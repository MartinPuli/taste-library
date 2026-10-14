# Stripe

Explicar servicios financieros con módulos de producto, datos y gradientes como recurso de identidad.

Esta nota propone un uso posible a partir de TasteLabs; falta contrastarla visualmente.

| Dato | Valor |
|---|---|
| Página | Homepage |
| Captura UTC | 2026-09-18T13:26:14.774070Z |
| Calidad | `extracted_unverified` |
| Uso sugerido | fintech, developer-tools |
| Recursos visuales | color-accent, modular |

## Datos para comparar

- Familias detectadas: sohne-var, monospace, SourceCodePro.
- Paleta registrada: #000000, #533AFD, #061B31, #50617A, #FFFFFF.
- Grilla: `{"columns": 12, "gutter": "16px", "max_width": "1264px"}`.
- Secciones disponibles: profile, layout, colors, typography, surfaces, elevation, interactions, actions, navigation, data_display, structure, icons, assets, sections.

Consultá las reglas de color y los roles tipográficos antes de tomar un valor aislado. Estos nombres de fuente no implican que sus archivos estén incluidos.

## Límites

- Secciones sin datos: brand_assets.

## Fuente y acceso

[Sitio](https://stripe.com/) · [Extracción](../data/raw/stripe.json) · [Tokens](../data/tokens/stripe.json)

```sh
python3 scripts/query.py show stripe --section layout
```

La URL de la captura, cuando existe, está en `result.artifacts` del archivo original.
