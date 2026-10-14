# Ghost

Estudiar el ritmo entre secciones oscuras y claras; la extracción no permite adoptar una paleta estructurada.

Esta nota propone un uso posible a partir de TasteLabs; falta contrastarla visualmente.

| Dato | Valor |
|---|---|
| Página | Homepage |
| Captura UTC | 2026-10-14T08:53:53.351064Z |
| Calidad | `limited` |
| Uso sugerido | hardware |
| Recursos visuales | cinematic, dark-technical |

## Datos para comparar

- Familias detectadas: Archivo, Archivo Narrow.
- Paleta registrada: sin valores.
- Grilla: `{"columns": 12, "gutter": "2rem", "max_width": "1512px"}`.
- Secciones disponibles: profile, layout, colors, typography, surfaces, elevation, interactions, actions, navigation, data_display, structure, icons, assets, brand_assets, sections.

Consultá las reglas de color y los roles tipográficos antes de tomar un valor aislado. Estos nombres de fuente no implican que sus archivos estén incluidos.

## Límites

- Paleta vacía en el resultado de TasteLabs; no se infieren colores.

## Fuente y acceso

[Sitio](https://ghost.ai/) · [Extracción](../data/raw/ghost.json) · [Tokens](../data/tokens/ghost.json)

```sh
python3 scripts/query.py show ghost --section layout
```

La URL de la captura, cuando existe, está en `result.artifacts` del archivo original.
