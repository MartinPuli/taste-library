# Framer

Mostrar la herramienta y sus resultados dentro de una página oscura con demostraciones de interfaz.

Esta nota propone un uso posible a partir de TasteLabs; falta contrastarla visualmente.

| Dato | Valor |
|---|---|
| Página | Homepage |
| Captura UTC | 2026-08-07T00:18:49.934442Z |
| Calidad | `extracted_unverified` |
| Uso sugerido | creative-tools |
| Recursos visuales | dark-technical, modular |

## Datos para comparar

- Familias detectadas: GT Walsheim Medium, Inter Variable, Inter, Input Mono Regular, sans-serif.
- Paleta registrada: #000000, #FFFFFF, #242424, #303030, #666666, #999999, #F3F3F3, #0099FF, #6600FF, #FF0066, #FD7702, #FFBB00, #4CD963, #22DDDD.
- Grilla: `{"columns": 12, "gutter": "40px", "max_width": "1200px"}`.
- Secciones disponibles: profile, layout, colors, typography, surfaces, elevation, interactions, actions, navigation, data_display, structure, icons, assets, sections.

Consultá las reglas de color y los roles tipográficos antes de tomar un valor aislado. Estos nombres de fuente no implican que sus archivos estén incluidos.

## Límites

- Secciones sin datos: brand_assets.

## Fuente y acceso

[Sitio](https://www.framer.com/) · [Extracción](../data/raw/framer.json) · [Tokens](../data/tokens/framer.json)

```sh
python3 scripts/query.py show framer --section layout
```

La URL de la captura, cuando existe, está en `result.artifacts` del archivo original.
