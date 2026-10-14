# MTS

Usar tramados, marcos y tipografía monoespaciada para dar identidad a una publicación técnica.

Esta nota propone un uso posible a partir de TasteLabs; falta contrastarla visualmente.

| Dato | Valor |
|---|---|
| Página | Homepage |
| Captura UTC | 2026-10-14T08:56:35.778602Z |
| Calidad | `extracted_unverified` |
| Uso sugerido | editorial-research, media-discovery |
| Recursos visuales | retro-digital, warm-editorial |

## Datos para comparar

- Familias detectadas: Chakra Petch, Iowan Old Style, SF Mono, System Default.
- Paleta registrada: #F2EFE6, #34D399, #181611, #869EF4, #5E5B55.
- Grilla: `{"columns": 12, "gutter": "2rem", "max_width": "1280px"}`.
- Secciones disponibles: profile, layout, colors, typography, surfaces, elevation, interactions, actions, navigation, data_display, structure, icons, assets, brand_assets, sections.

Consultá las reglas de color y los roles tipográficos antes de tomar un valor aislado. Estos nombres de fuente no implican que sus archivos estén incluidos.

## Límites

No registramos una incidencia específica; la extracción todavía no tiene revisión visual.

## Fuente y acceso

[Sitio](https://www.mts.now/) · [Extracción](../data/raw/mts.json) · [Tokens](../data/tokens/mts.json)

```sh
python3 scripts/query.py show mts --section layout
```

La URL de la captura, cuando existe, está en `result.artifacts` del archivo original.
