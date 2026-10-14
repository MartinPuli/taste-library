# Airbnb

Estudiar tarjetas de propiedades, navegación de búsqueda y fotografías que permiten comparar opciones.

Esta nota propone un uso posible a partir de TasteLabs; falta contrastarla visualmente.

| Dato | Valor |
|---|---|
| Página | Homepage |
| Captura UTC | 2026-10-08T15:15:43.471119Z |
| Calidad | `extracted_unverified` |
| Uso sugerido | hospitality, media-discovery |
| Recursos visuales | image-led, modular |

## Datos para comparar

- Familias detectadas: Airbnb Cereal VF.
- Paleta registrada: #222222, #6C6C6C, #FFFFFF, #C1C1C1, #000000.
- Grilla: `{"columns": 12, "gutter": "24px", "max_width": "1440px"}`.
- Secciones disponibles: profile, layout, colors, typography, surfaces, elevation, interactions, actions, navigation, data_display, structure, icons, assets, brand_assets, sections.

Consultá las reglas de color y los roles tipográficos antes de tomar un valor aislado. Estos nombres de fuente no implican que sus archivos estén incluidos.

## Límites

No registramos una incidencia específica; la extracción todavía no tiene revisión visual.

## Fuente y acceso

[Sitio](https://www.airbnb.com/) · [Extracción](../data/raw/airbnb.json) · [Tokens](../data/tokens/airbnb.json)

```sh
python3 scripts/query.py show airbnb --section layout
```

La URL de la captura, cuando existe, está en `result.artifacts` del archivo original.
