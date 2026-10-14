# Spotify

Dejar que portadas y artistas aporten color sobre superficies oscuras con navegación persistente.

Esta nota propone un uso posible a partir de TasteLabs; falta contrastarla visualmente.

| Dato | Valor |
|---|---|
| Página | Web Player Homepage |
| Captura UTC | 2026-10-08T15:15:36.464067Z |
| Calidad | `extracted_unverified` |
| Uso sugerido | media-discovery |
| Recursos visuales | dark-technical, image-led, modular |

## Datos para comparar

- Familias detectadas: SpotifyMixUITitle, SpotifyMixUI.
- Paleta registrada: #FFFFFF, #B3B3B3, #939393, #121212, #000000.
- Grilla: `{"columns": 12, "gutter": "16px", "max_width": "1199px"}`.
- Secciones disponibles: profile, layout, colors, typography, surfaces, elevation, interactions, actions, navigation, data_display, structure, icons, assets, brand_assets, sections.

Consultá las reglas de color y los roles tipográficos antes de tomar un valor aislado. Estos nombres de fuente no implican que sus archivos estén incluidos.

## Límites

No registramos una incidencia específica; la extracción todavía no tiene revisión visual.

## Fuente y acceso

[Sitio](https://www.spotify.com/) · [Extracción](../data/raw/spotify.json) · [Tokens](../data/tokens/spotify.json)

```sh
python3 scripts/query.py show spotify --section layout
```

La URL de la captura, cuando existe, está en `result.artifacts` del archivo original.
