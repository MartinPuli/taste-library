# Pinterest

Support visual discovery through grids and cards with little interface weight.

Suggested application based on the TasteLabs extraction. Treat it as editorial interpretation when comparing references.

| Field | Value |
|---|---|
| Cosign rank | 38 |
| Captured page | Homepage |
| Capture time (UTC) | 2026-10-14T05:06:49.351030Z |
| Suggested uses | media-discovery |
| Visual approach | image-led, modular |

## Details to compare

- Detected type families: Pin Sans, SF Mono.
- Recorded palette: #211922, #000000, #FFFFFF, #62625B, #91918C.
- Grid: `{"columns": 12, "gutter": "16px", "max_width": "1440px"}`.
- Available sections: profile, layout, colors, typography, surfaces, elevation, interactions, actions, navigation, data_display, structure, icons, assets, brand_assets, sections.

Read color rules and type roles before adopting an isolated value. Font names identify observed families; font files are not included. The source record and tokens carry the evidence metadata.

## Source and access

[Cosign ranking](https://cosign.co/questions/highest-taste-companies) · [Website](https://www.pinterest.com/) · [Extraction](../data/raw/pinterest.json) · [Tokens](../data/tokens/pinterest.json)

```sh
python3 scripts/query.py show pinterest --section layout
```

Screenshot links, when available, appear in `result.artifacts` in the extraction file.
