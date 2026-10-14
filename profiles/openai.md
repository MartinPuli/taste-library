# OpenAI

Revisar la captura antes de tomar valores: la extracción mezcla una descripción visual con fuentes de respaldo.

Esta nota propone un uso posible a partir de TasteLabs; falta contrastarla visualmente.

| Dato | Valor |
|---|---|
| Página | Homepage |
| Captura UTC | 2026-10-14T05:11:51.490971Z |
| Calidad | `limited` |
| Uso sugerido | editorial-research, creative-tools |
| Recursos visuales | modular |

## Datos para comparar

- Familias detectadas: Times New Roman, Arial, monospace.
- Paleta registrada: #000000, #0000EE, #F0F0F0, #767676, #101010.
- Grilla: `{"columns": 12, "gutter": "24px", "max_width": "1728px"}`.
- Secciones disponibles: profile, layout, colors, typography, surfaces, elevation, interactions, actions, navigation, data_display, structure, icons, assets, brand_assets, sections.

Consultá las reglas de color y los roles tipográficos antes de tomar un valor aislado. Estos nombres de fuente no implican que sus archivos estén incluidos.

## Límites

- Posible carga incompleta de estilos: se detectó Times New Roman. Revisar tipografía y colores contra la captura antes de usarlos.

## Fuente y acceso

[Sitio](https://openai.com/) · [Extracción](../data/raw/openai.json) · [Tokens](../data/tokens/openai.json)

```sh
python3 scripts/query.py show openai --section layout
```

La URL de la captura, cuando existe, está en `result.artifacts` del archivo original.
