# Pinterest

Permitir explorar contenido visual mediante grillas y tarjetas con poco peso de interfaz.

Esta nota propone un uso posible a partir de TasteLabs; falta contrastarla visualmente.

| Dato | Valor |
|---|---|
| Página | Homepage |
| Captura UTC | 2026-10-14T05:06:49.351030Z |
| Calidad | `extracted_unverified` |
| Uso sugerido | media-discovery |
| Recursos visuales | image-led, modular |

## Datos para comparar

- Familias detectadas: Pin Sans, SF Mono.
- Paleta registrada: #211922, #000000, #FFFFFF, #62625B, #91918C.
- Grilla: `{"columns": 12, "gutter": "16px", "max_width": "1440px"}`.
- Secciones disponibles: profile, layout, colors, typography, surfaces, elevation, interactions, actions, navigation, data_display, structure, icons, assets, brand_assets, sections.

Consultá las reglas de color y los roles tipográficos antes de tomar un valor aislado. Estos nombres de fuente no implican que sus archivos estén incluidos.

## Límites

No registramos una incidencia específica; la extracción todavía no tiene revisión visual.

## Fuente y acceso

[Sitio](https://www.pinterest.com/) · [Extracción](../data/raw/pinterest.json) · [Tokens](../data/tokens/pinterest.json)

```sh
python3 scripts/query.py show pinterest --section layout
```

La URL de la captura, cuando existe, está en `result.artifacts` del archivo original.
