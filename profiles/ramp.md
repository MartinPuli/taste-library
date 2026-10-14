# Ramp

Ordenar información financiera sobre fondos claros y reservar el acento amarillo para llamadas a la acción.

Esta nota propone un uso posible a partir de TasteLabs; falta contrastarla visualmente.

| Dato | Valor |
|---|---|
| Página | Homepage |
| Captura UTC | 2026-09-25T08:15:55.953997Z |
| Calidad | `extracted_unverified` |
| Uso sugerido | fintech |
| Recursos visuales | color-accent, modular |

## Datos para comparar

- Familias detectadas: System Sans, Inter, Lausanne.
- Paleta registrada: #FFFFFF, #0066FF, #E4F222, #1A1919.
- Grilla: `{"columns": 12, "gutter": "24px", "max_width": "1440px"}`.
- Secciones disponibles: profile, layout, colors, typography, surfaces, elevation, interactions, actions, navigation, data_display, structure, assets, sections.

Consultá las reglas de color y los roles tipográficos antes de tomar un valor aislado. Estos nombres de fuente no implican que sus archivos estén incluidos.

## Límites

- Secciones sin datos: icons, brand_assets.

## Fuente y acceso

[Sitio](https://ramp.com/) · [Extracción](../data/raw/ramp.json) · [Tokens](../data/tokens/ramp.json)

```sh
python3 scripts/query.py show ramp --section layout
```

La URL de la captura, cuando existe, está en `result.artifacts` del archivo original.
