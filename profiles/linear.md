# Linear

Organizar demostraciones de herramientas con paneles oscuros, bordes finos y jerarquía tipográfica.

Esta nota propone un uso posible a partir de TasteLabs; falta contrastarla visualmente.

| Dato | Valor |
|---|---|
| Página | Homepage |
| Captura UTC | 2026-10-10T10:50:53.682721Z |
| Calidad | `extracted_unverified` |
| Uso sugerido | developer-tools, productivity |
| Recursos visuales | dark-technical, modular |

## Datos para comparar

- Familias detectadas: Inter Variable, Berkeley Mono.
- Paleta registrada: #F7F8F8, #D0D6E0, #8A8F98, #62666D, #08090A.
- Grilla: `{"columns": 12, "gutter": "32px", "max_width": "calc(1344px + 46px * 2)"}`.
- Secciones disponibles: profile, layout, colors, typography, surfaces, elevation, interactions, actions, navigation, data_display, structure, icons, assets, brand_assets, sections.

Consultá las reglas de color y los roles tipográficos antes de tomar un valor aislado. Estos nombres de fuente no implican que sus archivos estén incluidos.

## Límites

No registramos una incidencia específica; la extracción todavía no tiene revisión visual.

## Fuente y acceso

[Sitio](https://linear.app/) · [Extracción](../data/raw/linear.json) · [Tokens](../data/tokens/linear.json)

```sh
python3 scripts/query.py show linear --section layout
```

La URL de la captura, cuando existe, está en `result.artifacts` del archivo original.
