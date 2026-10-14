# Pangram

Estudiar fondos crema, bloques de datos y acentos de color en un producto de detección de texto.

Esta nota propone un uso posible a partir de TasteLabs; falta contrastarla visualmente.

| Dato | Valor |
|---|---|
| Página | Homepage |
| Captura UTC | 2026-09-23T23:13:42.526672Z |
| Calidad | `extracted_unverified` |
| Uso sugerido | editorial-research, productivity |
| Recursos visuales | warm-editorial, color-accent |

## Datos para comparar

- Familias detectadas: headingFont, IBM Plex Sans, IBM Plex Mono, Imbue.
- Paleta registrada: #14201E, #E2E8F0, #000000, #777777, #FF6106.
- Grilla: `{"columns": 12, "gutter": "2rem", "max_width": "1280px"}`.
- Secciones disponibles: profile, layout, colors, typography, surfaces, elevation, interactions, actions, navigation, data_display, structure, icons, assets, sections.

Consultá las reglas de color y los roles tipográficos antes de tomar un valor aislado. Estos nombres de fuente no implican que sus archivos estén incluidos.

## Límites

- Secciones sin datos: brand_assets.

## Fuente y acceso

[Sitio](https://www.pangram.com/) · [Extracción](../data/raw/pangram.json) · [Tokens](../data/tokens/pangram.json)

```sh
python3 scripts/query.py show pangram --section layout
```

La URL de la captura, cuando existe, está en `result.artifacts` del archivo original.
