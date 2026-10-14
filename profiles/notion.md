# Notion

Combinar capturas del producto con ilustraciones para explicar tareas sin llenar la página de controles.

Esta nota propone un uso posible a partir de TasteLabs; falta contrastarla visualmente.

| Dato | Valor |
|---|---|
| Página | Homepage |
| Captura UTC | 2026-10-08T00:42:08.521274Z |
| Calidad | `extracted_unverified` |
| Uso sugerido | productivity |
| Recursos visuales | warm-editorial, modular |

## Datos para comparar

- Familias detectadas: NotionInter, Lyon Text, iA Writer Mono, Permanent Marker.
- Paleta registrada: #000000, #FFFFFF, #615D59, #A39E98, #097FE8.
- Grilla: `{"columns": 12, "gutter": "28px", "max_width": "1464px"}`.
- Secciones disponibles: profile, layout, colors, typography, surfaces, elevation, interactions, actions, navigation, data_display, structure, icons, assets, brand_assets, sections.

Consultá las reglas de color y los roles tipográficos antes de tomar un valor aislado. Estos nombres de fuente no implican que sus archivos estén incluidos.

## Límites

No registramos una incidencia específica; la extracción todavía no tiene revisión visual.

## Fuente y acceso

[Sitio](https://www.notion.com/) · [Extracción](../data/raw/notion.json) · [Tokens](../data/tokens/notion.json)

```sh
python3 scripts/query.py show notion --section layout
```

La URL de la captura, cuando existe, está en `result.artifacts` del archivo original.
