# Twitter

Estudiar solo la jerarquía de acceso y registro de X; la captura no describe el feed.

Esta nota propone un uso posible a partir de TasteLabs; falta contrastarla visualmente.

| Dato | Valor |
|---|---|
| Página | Login/Signup Page |
| Captura UTC | 2026-10-14T08:54:30.833239Z |
| Calidad | `extracted_unverified` |
| Uso sugerido | authentication |
| Recursos visuales | monochrome |

## Datos para comparar

- Familias detectadas: TwitterChirp, SFMono-Regular.
- Paleta registrada: #0F141A, #000000, #E4EAEC, #79716B, #3C4043.
- Grilla: `{"columns": 12, "gutter": "1rem", "max_width": "80rem"}`.
- Secciones disponibles: profile, layout, colors, typography, surfaces, elevation, interactions, actions, navigation, data_display, structure, icons, assets, brand_assets, sections.

Consultá las reglas de color y los roles tipográficos antes de tomar un valor aislado. Estos nombres de fuente no implican que sus archivos estén incluidos.

## Límites

- La extracción corresponde al acceso público de X, no al feed ni a la antigua identidad de Twitter.

## Fuente y acceso

[Sitio](https://x.com/) · [Extracción](../data/raw/twitter.json) · [Tokens](../data/tokens/twitter.json)

```sh
python3 scripts/query.py show twitter --section layout
```

La URL de la captura, cuando existe, está en `result.artifacts` del archivo original.
