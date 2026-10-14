# Core Automation

Ordenar mensajes de investigación con títulos grandes, marcos y bloques geométricos.

Esta nota propone un uso posible a partir de TasteLabs; falta contrastarla visualmente.

| Dato | Valor |
|---|---|
| Página | Homepage |
| Captura UTC | 2026-10-14T08:55:43.902911Z |
| Calidad | `extracted_unverified` |
| Uso sugerido | editorial-research |
| Recursos visuales | modular, monochrome |

## Datos para comparar

- Familias detectadas: Helvetica, Berkeley Mono, SF Mono, ui-monospace.
- Paleta registrada: #111111, #000000, #FF2D09, #699EFF, #ECECEC.
- Grilla: `{"columns": 12, "gutter": "34px", "max_width": "1080px"}`.
- Secciones disponibles: profile, layout, colors, typography, surfaces, elevation, interactions, actions, navigation, data_display, structure, icons, assets, brand_assets, sections.

Consultá las reglas de color y los roles tipográficos antes de tomar un valor aislado. Estos nombres de fuente no implican que sus archivos estén incluidos.

## Límites

No registramos una incidencia específica; la extracción todavía no tiene revisión visual.

## Fuente y acceso

[Sitio](https://www.coreauto.com/) · [Extracción](../data/raw/core-automation.json) · [Tokens](../data/tokens/core-automation.json)

```sh
python3 scripts/query.py show core-automation --section layout
```

La URL de la captura, cuando existe, está en `result.artifacts` del archivo original.
