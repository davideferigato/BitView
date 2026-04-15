# BitView – 00-99 Redstone Display in Minecraft

**BitView** is a fully functional two‑digit decimal display built inside Minecraft using pure redstone logic.  
It demonstrates the practical application of Boolean algebra, Karnaugh maps, and logic minimization on a highly constrained hardware platform (redstone torches and dust).

## Key Features
- Displays numbers from **00 to 99** on two side‑by‑side 7‑segment displays.
- Input via **18 levers** (1–9 for units, 1–9 for tens). Zero is the default state.
- Each digit is driven by an identical circuit derived from **minimized Boolean expressions** (obtained via Karnaugh maps).
- Logic implemented using **only NOT and OR gates** (the only reliable gates in redstone) via De Morgan transformations.
- The entire circuit is **stacked vertically** to keep the world compact and readable.

## Repository Structure
- **`world/`** – The Minecraft save folder (`BitView_00-99_Display`). Copy it into your `.minecraft/saves` folder to play.
- **`screenshots/`** – In‑game screenshots showing the lever panel, the circuit layers, and the display in action.
- **`video/`** – A short demonstration video (`record test.mp4`).
- **`circuit docs/`** – Technical documentation: truth table, Karnaugh maps, logic circuit diagrams, and the conversion from AND/OR to NOT/OR.
- **`coder docs/`** – Schematics for the 1‑to‑9 encoder used in the input stage.

## How to Use the World
1. Download or clone this repository.
2. Copy the folder `world/BitView_00-99_Display` into your Minecraft `saves` directory.
3. Launch Minecraft, select the world **BitView – 00-99 Display**, and enter.
4. Use the 18 levers (9 on the left for tens, 9 on the right for units) to compose any number from 00 to 99.
5. To show **0** in a digit, simply leave all levers in that row untouched.

## Project Evolution
This repository also contains two earlier (unoptimized) versions for comparison:
- **`first_attempt_single_display/`** – A single‑digit 0‑9 display with non‑minimized logic.
- **`second_attempt_double_display/`** – A two‑digit 00‑99 display using the same unoptimized logic.

These show the iterative improvement process and the importance of Boolean minimization when working with redstone.

## Hexadecimal Extension
The folder **`hexadecimal_circuit/`** contains a complete theoretical design for a hexadecimal decoder (0‑9, A‑F). It includes truth tables, Karnaugh maps, minimized expressions, and circuit schematics. The design is fully worked out but was not built in Minecraft due to the excessive wiring complexity in 3D.

## Why Only NOT and OR?
Minecraft redstone provides two basic logic components:
- **Redstone torch** → NOT gate (output ON when input OFF).
- **Redstone dust** → OR gate (output ON if any input is ON).

AND gates are simulated using De Morgan’s law:  
`A AND B = NOT( (NOT A) OR (NOT B) )`  
All expressions in this project were converted to this NOT‑OR form. See `circuit docs/AND to OR-NOT.md` for a detailed explanation.

## License
This project is open source and available under the MIT License.