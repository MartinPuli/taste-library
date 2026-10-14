# Wander

Dar espacio a las fotos de alojamientos y usar controles discretos para explorar y comparar.

Esta nota propone un uso posible a partir de TasteLabs; falta contrastarla visualmente.

| Dato | Valor |
|---|---|
| Página | Homepage |
| Captura UTC | 2026-10-14T08:56:06.649511Z |
| Calidad | `extracted_unverified` |
| Uso sugerido | hospitality |
| Recursos visuales | image-led, warm-editorial |

## Datos para comparar

- Familias detectadas: instrumentSans, SFMono-Regular.
- Paleta registrada: #202020, #000000, #636363, #F7F7F7, #008433.
- Grilla: `{"columns": 12, "gutter": "2rem", "max_width": "1832px"}`.
- Secciones disponibles: profile, layout, colors, typography, surfaces, elevation, interactions, actions, navigation, data_display, structure, assets, brand_assets, sections.

Consultá las reglas de color y los roles tipográficos antes de tomar un valor aislado. Estos nombres de fuente no implican que sus archivos estén incluidos.

## Límites

- Secciones sin datos: icons.

## Fuente y acceso

[Sitio](https://www.wander.com/) · [Extracción](../data/raw/wander.json) · [Tokens](../data/tokens/wander.json)

```sh
python3 scripts/query.py show wander --section layout
```

La URL de la captura, cuando existe, está en `result.artifacts` del archivo original.
