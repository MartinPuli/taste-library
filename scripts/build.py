#!/usr/bin/env python3
"""Generate compact indexes, section files and profiles for agents."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
COMPONENT_TYPES = {'button':'buttons', 'card':'cards', 'navigation':'navigation',
                   'form':'forms', 'carousel':'carousels', 'accordion':'accordions',
                   'video':'video', 'logo_strip':'logo-strips'}
STRUCTURED = {'buttons':('actions','button_list'), 'navigation':('navigation','top_nav'),
              'cards':('data_display','tiles'), 'tables':('data_display','tables'),
              'charts':('data_display','charts'), 'accordions':('structure','accordion')}
CONTENT = {
    'hardware':'Product photography with enough detail and consistent framing to carry large sections.',
    'developer-tools':'A real product workflow, readable interface examples, and a clear first action for developers.',
    'editorial-research':'A small set of strong headlines and substantial articles or research to support the hierarchy.',
    'creative-tools':'Representative work samples and a real demonstration of the creation workflow.',
    'media-discovery':'A collection of labeled images or media that readers can browse and compare.',
    'fintech':'Concrete product screens and a clearly explained financial workflow.',
    'hospitality':'Consistent property photography and useful details such as location and booking context.',
    'productivity':'Real workspace content that makes the product demonstration understandable.',
    'authentication':'The actual account-entry options and form requirements for your product.',
}

def read(path):
    return json.loads((ROOT/path).read_text())

def write(path, data):
    dest=ROOT/path
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(json.dumps(data, ensure_ascii=False, indent=2)+'\n')

def present(value):
    if isinstance(value, dict):
        return any(present(v) for v in value.values())
    if isinstance(value, list):
        return any(present(v) for v in value)
    return value is not None and value != ''

def component_evidence(system):
    found={}
    for name,(section,key) in STRUCTURED.items():
        if present((system.get(section) or {}).get(key)):
            found.setdefault(name,[]).append({'section':section, 'pointer':f'/{key}'})
    for i,section in enumerate(system.get('sections') or []):
        for j,component in enumerate(section.get('components') or []):
            name=COMPONENT_TYPES.get(component.get('type'))
            if name:
                found.setdefault(name,[]).append({'section':'sections','pointer':f'/{i}/components/{j}'})
    return found

def build():
    catalog=read('catalog/index.json')
    taxonomy=read('catalog/taxonomy.json')
    for entry in catalog['entries']:
        id=entry['id']
        raw=read(entry['paths']['raw'])
        system=raw['result']['design_system']
        review=read(f'data/reviews/{id}.json')
        evidence=component_evidence(system)
        entry['components']=sorted(evidence)
        entry['component_evidence']=evidence
        entry['sections']={k:{'path':f'data/sections/{id}/{k}.json','has_data':present(v)} for k,v in system.items()}
        entry['paths']['review']=f'data/reviews/{id}.json'
        entry['note_basis']='Editorial recommendation; see the saved-capture review for its scope.'
        entry['review_status']='saved_capture_reviewed'
        entry['preview']=f'data/previews/{id}.webp'
        for key,value in system.items():
            write(entry['sections'][key]['path'],{
                'id':id,'source_url':entry['source_url'],'captured_at':entry['captured_at'],
                'quality':entry['quality'],'warnings':entry['warnings'],'section':key,
                'has_data':present(value),'source_file':entry['paths']['raw'],
                'source_pointer':f'/result/design_system/{key}','review_file':entry['paths']['review'],
                'data':value})
        requirement=CONTENT[entry['use_cases'][0]]
        recommendations=[
            {'text':entry['selection_note'],'evidence':['layout','sections'],'kind':'editorial'},
            {'text':'Adapt the documented controls to your own primary action and labels; retain only states your interface needs.',
             'evidence':['actions'],'kind':'editorial'}
        ]
        if not present(system.get('actions')):
            recommendations=recommendations[:1]
        body=f"# {entry['name']}\n\n{entry['selection_note']}\n\n"
        body+=f"Cosign rank {entry['rank']} · Captured {entry['captured_at']} · {entry['page_type']}\n\n"
        body+=f"[Original website]({entry['source_url']}) · [Full extraction](../{entry['paths']['raw']}) · [Review record](../{entry['paths']['review']})\n\n"
        capture=raw['result']['artifacts'].get('full_page_screenshot') or raw['result']['artifacts'].get('screenshot')
        body+=f"[Small visual preview](../{entry['preview']}) · [Original saved capture]({capture['url']})\n\n"
        body+="## What the saved capture shows\n\n"+review['visual_observation']+"\n\n"
        artifact_labels={'html':'HTML', 'css':'CSS', 'screenshot':'Viewport screenshot',
                         'full_page_screenshot':'Full-page screenshot', 'element_layout':'Element layout'}
        artifact_links=[f"[{artifact_labels.get(kind,kind)}]({artifact['url']})"
                        for kind,artifact in raw['result']['artifacts'].items() if artifact]
        body+="## Original captured files\n\n"+' · '.join(artifact_links)+"\n\n"
        body+="These links open the original files hosted by TasteLabs. The full extraction preserves their metadata and any unavailable values.\n\n"
        body+="## Where to use it\n\nProject types: "+', '.join(entry['use_cases'])+". Styles: "+', '.join(entry['styles'])+". These are editorial tags.\n\n"
        body+="## Patterns to adapt\n\n"
        for rec in recommendations:
            refs=[f"[{s}](../{entry['sections'][s]['path']})" for s in rec['evidence'] if s in entry['sections']]
            body+="- "+rec['text']+" Evidence: "+', '.join(refs)+".\n"
        body+="\n## Content to bring\n\n"+requirement+" This is an editorial prerequisite for adapting the reference, not an extracted brand rule.\n\n"
        body+="## Read only what you need\n\n"
        body+='\n'.join(f"- [{key.replace('_',' ').title()}](../{v['path']})"+(' · no observed data' if not v['has_data'] else '') for key,v in entry['sections'].items())+'\n\n'
        body+="## Evidence scope\n\n"+review['scope']+"\n\n"
        body+="Extraction status: "+chr(96)+entry['quality']+chr(96)+". Review notes do not certify an entire design system. Missing values remain missing.\n"
        (ROOT/entry['paths']['profile']).write_text(body)
    catalog['schema_version']='1.1'
    catalog['counts']={'records':len(catalog['entries']),
                       'default_references':sum(e['quality']!='limited' for e in catalog['entries']),
                       'saved_capture_reviews':len(catalog['entries'])}
    taxonomy['quality']['extracted_unverified']='Extracted values; see each review record for the specific checks performed. Not a fully verified design system.'
    taxonomy['components']=sorted({c for e in catalog['entries'] for c in e['components']})
    write('catalog/index.json',catalog)
    write('catalog/taxonomy.json',taxonomy)
    summary_keys=['id','name','rank','use_cases','styles','components','quality','selection_note']
    write('catalog/search.json',{'counts':catalog['counts'],'entries':[
        dict({k:e[k] for k in summary_keys},profile=e['paths']['profile']) for e in catalog['entries']]})
    table="# Reference index\n\n"+f"{catalog['counts']['default_references']} references in default search; {catalog['counts']['records']} source records from Cosign’s top 40.\n\n"
    table+="| Rank | Reference | Project types | Styles | Components | Evidence |\n|---|---|---|---|---|---|\n"
    for e in catalog['entries']:
        table+=f"| {e['rank']} | [{e['name']}](../{e['paths']['profile']}) | {', '.join(e['use_cases'])} | {', '.join(e['styles'])} | {', '.join(e['components'])} | {e['quality']} |\n"
    (ROOT/'catalog/INDEX.md').write_text(table)
    for kind,filename in [('use_cases','by-use-case'),('styles','by-style'),('components','by-component')]:
        lines=['# References by '+kind.replace('_',' ')]
        for tag in taxonomy[kind]:
            lines+=['','## '+tag,'']
            lines += [f"- [{e['name']}](../{e['paths']['profile']}): {e['selection_note']}" for e in catalog['entries'] if tag in e[kind]]
        (ROOT/f'catalog/{filename}.md').write_text('\n'.join(lines)+'\n')
    for filename in ['README.md','social/launch-post.md']:
        path=ROOT/filename
        if path.exists():
            import re
            text=path.read_text()
            text=re.sub(r'<!-- count:default -->\d+<!-- /count -->',f"<!-- count:default -->{catalog['counts']['default_references']}<!-- /count -->",text)
            path.write_text(text)
    print(f"Built {len(catalog['entries'])} references and {sum(len(e['sections']) for e in catalog['entries'])} section files.")

if __name__=='__main__':
    build()
