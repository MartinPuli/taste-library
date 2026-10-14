# Figma

Separar la interfaz de las muestras de trabajo mediante bloques y acentos de color.

Esta nota propone un uso posible a partir de TasteLabs; falta contrastarla visualmente.

| Dato | Valor |
|---|---|
| Página | Homepage |
| Captura UTC | 2026-09-15T16:36:48.597923Z |
| Calidad | `extracted_unverified` |
| Uso sugerido | creative-tools |
| Recursos visuales | color-accent, modular |

## Datos para comparar

- Familias detectadas: figmaSans, figmaMono.
- Paleta registrada: #000000, #FFFFFF, #00B6FF, #24CB71, #FF7237.
- Grilla: `{"columns": 12, "gutter": "1rem", "max_width": "95rem"}`.
- Secciones disponibles: profile, layout, colors, typography, surfaces, elevation, interactions, actions, navigation, data_display, structure, icons, assets, sections.

Consultá las reglas de color y los roles tipográficos antes de tomar un valor aislado. Estos nombres de fuente no implican que sus archivos estén incluidos.

## Límites

- Secciones sin datos: brand_assets.

## Fuente y acceso

[Sitio](https://www.figma.com/) · [Extracción](../data/raw/figma.json) · [Tokens](../data/tokens/figma.json)

```sh
python3 scripts/query.py show figma --section layout
```

La URL de la captura, cuando existe, está en `result.artifacts` del archivo original.
