# SpaceX

Presentar maquinaria e ingeniería con imágenes de gran escala y títulos en mayúsculas.

Esta nota propone un uso posible a partir de TasteLabs; falta contrastarla visualmente.

| Dato | Valor |
|---|---|
| Página | Homepage |
| Captura UTC | 2026-07-23T01:41:07.004114Z |
| Calidad | `extracted_unverified` |
| Uso sugerido | hardware |
| Recursos visuales | cinematic, dark-technical |

## Datos para comparar

- Familias detectadas: D-DIN-Bold, D-DIN, Roboto Mono.
- Paleta registrada: #000000, #F0F0FA, #252628, #FFFFFF, #01579B, #CCCCCC.
- Grilla: `{"columns": 12, "gutter": "40px", "max_width": "1700px"}`.
- Secciones disponibles: profile, layout, colors, typography, surfaces, elevation, interactions, actions, navigation, data_display, structure, icons, assets, sections.

Consultá las reglas de color y los roles tipográficos antes de tomar un valor aislado. Estos nombres de fuente no implican que sus archivos estén incluidos.

## Límites

- Secciones sin datos: brand_assets.

## Fuente y acceso

[Sitio](https://www.spacex.com/) · [Extracción](../data/raw/spacex.json) · [Tokens](../data/tokens/spacex.json)

```sh
python3 scripts/query.py show spacex --section layout
```

La URL de la captura, cuando existe, está en `result.artifacts` del archivo original.
