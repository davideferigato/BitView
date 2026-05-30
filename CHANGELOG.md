# Changelog

All notable changes to the BitView project are documented in this file.

## [1.0.0] – Final Optimised 00-99 Display
- Initial release of fully optimised two‑digit decimal display.
- Minimised Boolean expressions derived from Karnaugh maps.
- Converted to only NOT and OR gates (De Morgan).
- Vertical stacking: units layer below, tens layer above.
- Displays side‑by‑side, keypad 3×3 lever blocks.
- Full documentation: truth tables, K‑maps, logic diagrams.

## [0.2.0] – Legacy Double Digit (00-99 Unoptimised)
- Second attempt: two‑digit display using unoptimised logic.
- Same vertical layering as final version but with redundant gates.
- 100‑lever keypad (00-99) partially wired due to complexity.
- Fully playable, but larger and slower.

## [0.1.0] – Legacy Single Digit (0-9 Unoptimised)
- First attempt: single‑digit 0‑9 display with non‑minimised expressions.
- Input via 10 levers (0-9).
- Works correctly but inefficient (more gates, longer signal paths).
- Served as proof of concept and learning base.

[1.0.0]: https://github.com/davideFerigato/BitView/releases/tag/v1.0
[0.2.0]: https://github.com/davideFerigato/BitView/releases/tag/v0.2
[0.1.0]: https://github.com/davideFerigato/BitView/releases/tag/v0.1
