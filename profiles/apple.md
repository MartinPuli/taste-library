# Apple

Estudiar la escala de las fotos de producto y la alternancia de fondos para separar lanzamientos.

Esta nota propone un uso posible a partir de TasteLabs; falta contrastarla visualmente.

| Dato | Valor |
|---|---|
| Página | Homepage |
| Captura UTC | 2026-09-24T14:14:29.940321Z |
| Calidad | `extracted_unverified` |
| Uso sugerido | hardware |
| Recursos visuales | cinematic, monochrome, image-led |

## Datos para comparar

- Familias detectadas: SF Pro Display, SF Pro Text.
- Paleta registrada: #1D1D1F, #000000, #2997FF, #F5F5F7, #6E6E73.
- Grilla: `{"columns": 12, "gutter": "2rem", "max_width": "1024px"}`.
- Secciones disponibles: profile, layout, colors, typography, surfaces, elevation, interactions, actions, navigation, data_display, structure, icons, assets, sections.

Consultá las reglas de color y los roles tipográficos antes de tomar un valor aislado. Estos nombres de fuente no implican que sus archivos estén incluidos.

## Límites

- Secciones sin datos: brand_assets.

## Fuente y acceso

[Sitio](https://www.apple.com/) · [Extracción](../data/raw/apple.json) · [Tokens](../data/tokens/apple.json)

```sh
python3 scripts/query.py show apple --section layout
```

La URL de la captura, cuando existe, está en `result.artifacts` del archivo original.
