# taste-library

40 referencias de diseño para que un agente pueda elegir una dirección antes de construir una interfaz.

La colección parte del [ranking de Cosign](https://cosign.co/questions/highest-taste-companies), consultado el 14 de octubre de 2026, y de extracciones de TasteLabs. Cada empresa tiene una ficha corta, sus datos de diseño y la fecha de captura. El número del ranking sirve como referencia de origen; no decide qué diseño encaja con un proyecto.

## Por dónde empezar

Leé [AGENTS.md](AGENTS.md) y [el índice](catalog/INDEX.md). Si ya tenés un brief, buscá por estilo o uso:

```sh
python3 scripts/query.py search 'cálido editorial' --limit 5
python3 scripts/query.py search --use-case developer-tools --style dark-technical
python3 scripts/query.py show linear
python3 scripts/query.py show linear --section typography
```

No requiere instalar dependencias. La búsqueda compara palabras y etiquetas, con equivalencias básicas como «cálido» y `warm`; no usa embeddings ni llama a un modelo. Agregá `--json` a `search` para recibir resultados estructurados.

Para justificar una elección, usá la [guía de selección](guides/selection.md). Pide comparar candidatas contra el brief y citar qué parte de cada referencia querés adoptar. La [plantilla de decisión](guides/decision-template.md) deja esa elección por escrito.

## Archivos

| Ruta | Contenido |
|---|---|
| [catalog/index.json](catalog/index.json) | Índice para agentes: usos, estilos, calidad y rutas de cada referencia |
| [catalog/INDEX.md](catalog/INDEX.md) | Las 40 empresas en una tabla |
| [catalog/by-use-case.md](catalog/by-use-case.md) | Referencias agrupadas por tipo de proyecto |
| [catalog/by-style.md](catalog/by-style.md) | Referencias agrupadas por recursos visuales |
| `profiles/<id>.md` | Ficha breve para comparar sin leer toda la extracción |
| `data/tokens/<id>.json` | Colores, tipografía, grilla y breakpoints extraídos |
| `data/raw/<id>.json` | Sistema completo y enlaces a artefactos de TasteLabs |
| [data/manifest.json](data/manifest.json) | Fechas, origen y hashes de los archivos |

Los identificadores, como `linear` o `teenage-engineering`, no dependen de su posición en el ranking. [llms.txt](llms.txt) reúne los puntos de entrada para herramientas que usan ese formato.

## Qué tan confiable es

TasteLabs analiza páginas públicas; esta biblioteca no contiene los manuales oficiales de las empresas. Las categorías de uso y las notas de las fichas son nuestra interpretación de sus extracciones. Todavía falta contrastarlas visualmente una por una.

OpenAI tiene posibles estilos de respaldo y Ghost devolvió la paleta vacía. La búsqueda los excluye por defecto; `--include-limited` permite consultarlos. X corresponde a su página de acceso y Perplexity a su interfaz pública de búsqueda. Los avisos acompañan a cada resultado, también en los tokens.

Conservamos 20 extracciones anteriores y agregamos 20 solicitudes. Algunas usaron la caché de TasteLabs: la fecha de captura puede ser anterior a la fecha del ranking. Los enlaces a capturas y archivos remotos pueden dejar de funcionar.

## Mantener la colección

```sh
python3 scripts/validate.py
python3 -m unittest discover -s tests
```

[La guía de mantenimiento](guides/maintenance.md) explica cómo agregar una marca sin perder la fuente ni mezclar observaciones con recomendaciones. [RIGHTS.md](RIGHTS.md) aclara el alcance de los materiales de terceros.
