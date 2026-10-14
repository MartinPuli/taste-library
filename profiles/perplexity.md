# Perplexity

Concentrar la página alrededor de la búsqueda y dejar las funciones secundarias en segundo plano.

Esta nota propone un uso posible a partir de TasteLabs; falta contrastarla visualmente.

| Dato | Valor |
|---|---|
| Página | Search Interface |
| Captura UTC | 2026-10-14T08:54:30.860526Z |
| Calidad | `extracted_unverified` |
| Uso sugerido | productivity |
| Recursos visuales | warm-editorial, modular |

## Datos para comparar

- Familias detectadas: System Sans.
- Paleta registrada: #FBFBFB, #1A73E8, #252525, #0B2833, #000000.
- Grilla: `{"columns": 12, "gutter": "0.75rem", "max_width": "768px"}`.
- Secciones disponibles: profile, layout, colors, typography, surfaces, elevation, interactions, actions, navigation, data_display, structure, icons, assets, brand_assets, sections.

Consultá las reglas de color y los roles tipográficos antes de tomar un valor aislado. Estos nombres de fuente no implican que sus archivos estén incluidos.

## Límites

- Interfaz pública de búsqueda; no cubre todas las pantallas del producto.

## Fuente y acceso

[Sitio](https://perplexity.ai/) · [Extracción](../data/raw/perplexity.json) · [Tokens](../data/tokens/perplexity.json)

```sh
python3 scripts/query.py show perplexity --section layout
```

La URL de la captura, cuando existe, está en `result.artifacts` del archivo original.
