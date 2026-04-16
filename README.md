# BitView – 00-99 Redstone Display in Minecraft

![Minecraft Version](https://img.shields.io/badge/Minecraft-Java%20Edition%201.20.4-blue?logo=minecraft)
![License](https://img.shields.io/badge/License-MIT-green)
![Release](https://img.shields.io/badge/Release-v1.0-orange)
![Build Status](https://github.com/davideFerigato/BitView/actions/workflows/blank.yml/badge.svg)


**BitView** is a fully functional two‑digit decimal display built inside **Minecraft** using pure redstone logic.  
It demonstrates the practical application of **Boolean algebra**, **Karnaugh maps**, and **logic minimization** on a highly constrained hardware platform (redstone torches and dust).

---

## 🚀 Quick Navigation

- [Getting Started](#-getting-started)
- [Key Features](#-key-features)
- [Gallery](#-gallery)
- [Video Demo](#-video-demo)
- [Repository Structure](#-repository-structure)
- [How It Works](#-how-it-works)
- [Why Only NOT and OR?](#-why-only-not-and-or)
- [Project Evolution](#-project-evolution)
- [Hexadecimal Extension](#-hexadecimal-extension)
- [Legacy Attempts vs Final](#-legacy-attempts-vs-final)
- [Credits](#-credits)
- [License](#-license)

---

## 📦 Getting Started

### Requirements
- **Minecraft: Java Edition** (version 1.20.4 or newer, but 1.20+ should work)
- No mods or datapacks required – pure vanilla.

### How to Install the World
1. Download or clone this repository.
2. Copy the folder `world/BitView_00-99_Display` into your Minecraft `saves` directory:
   - **Windows**: `%APPDATA%\.minecraft\saves`
   - **macOS**: `~/Library/Application Support/minecraft/saves`
   - **Linux**: `~/.minecraft/saves`
3. Launch Minecraft, select the world **BitView – 00-99 Display**, and enter.

## How to Use the Display

The physical structure is organised in **vertical layers**:
- **Bottom layer** → units digit circuit
- **Layer above** → tens digit circuit
- (Higher layers could be added for hundreds, thousands, etc.)

The **displays** are placed **side by side** (tens on the left, units on the right) to form a normal two‑digit number.

The **keypad** consists of two **3×3 lever blocks** (digits 1–9), stacked vertically:
- **Bottom 3×3 block** → selects the **units** digit (1–9)
- **Upper 3×3 block** → selects the **tens** digit (1–9)

### How to compose a number:
1. **Tens digit** – pull any lever in the **upper** 3×3 block (1–9).
2. **Units digit** – pull any lever in the **lower** 3×3 block (1–9).
3. **Zero** is the default state – to display 0 in a digit, leave **all levers in that block untouched**.
4. Pull any combination to display a number from **00 to 99**.

### Example:
- To show **53**:  
  Pull lever `5` in the **upper** (tens) block.  
  Pull lever `3` in the **lower** (units) block.  
  The left display shows `5`, the right display shows `3`.

- To show **7** (as `07`):  
  Pull lever `7` in the **lower** (units) block.  
  Leave the **upper** (tens) block untouched → left display shows `0`.

---

## ✨ Key Features

- Displays numbers from **00 to 99** on two side‑by‑side 7‑segment displays.
- Input via **18 levers** (1–9 for units, 1–9 for tens). Zero is the default state.
- Each digit is driven by an identical circuit derived from **minimized Boolean expressions** (obtained via Karnaugh maps).
- Logic implemented using **only NOT and OR gates** (the only reliable gates in redstone) via De Morgan transformations.
- The entire circuit is **stacked vertically** to keep the world compact and readable.
- Fully documented with truth tables, K‑maps, logic diagrams, and conversion to NOT/OR.

---

## 🖼️ Gallery

| Encoder part | Main circuit | Display example: 51 |
|-------------|----------------|----------------------|
| ![encoder view](./00-99_Display/screenshots/encoder%20view.png) | ![circuit view](./00-99_Display/screenshots/circuit%20view.png) | ![test 51](./00-99_Display/screenshots/test%2051.png) |

| Display: 92 | Display: 99 | Full overview |
|-------------|-------------|----------------|
| ![test 92](./00-99_Display/screenshots/test%2092.png) | ![test 99](./00-99_Display/screenshots/test%2099.png) | ![full view](./00-99_Display/screenshots/full%20view.png) |

More screenshots can be found in the [`screenshots/`](./00-99_Display/screenshots) folder.

---

## 🎥 Video Demo

A short demonstration of the display in action:  
[`record test.mp4`](./00-99_Display/video/record%20test.mp4) *(download to watch)*

---

## 📁 Repository Structure

```
BitView/
├── world/                          # Minecraft save folder (BitView_00-99_Display)
├── screenshots/                    # In‑game screenshots
├── video/                          # Demo video (record test.mp4)
├── circuit docs/                   # Technical documentation
│   ├── truth table.csv
│   ├── karnaugh maps.pdf
│   ├── karnaugh maps.tex
│   ├── logic circuit.drawio
│   ├── logic circuit.jpg
│   └── AND to OR-NOT.md
├── encoder docs/                     # Schematics for the 1‑to‑9 encoder
│   ├── encoder1-9.drawio
│   └── encoder1-9.jpg
├── legacy_attempts/                # Earlier unoptimized versions
│   ├── first_attempt_single_display/
│   ├── second_attempt_double_display/
│   └── hexadecimal_circuit/
├── README.md
└── LICENSE
```

👉 Explore the folders directly from this repository.

---

## ⚙️ How It Works

1. **Input encoding** – Each lever directly selects a decimal digit (no binary conversion on the lever side).  
2. **Binary‑coded decimal (BCD)** – The lever signals are encoded into 4‑bit BCD inside the circuit.  
3. **Karnaugh maps** – For each of the 7 segments (a–g), a truth table for inputs 0–9 was built.  
4. **Minimization** – K‑maps produced minimal AND‑OR expressions.  
5. **NOT/OR conversion** – Using De Morgan’s law, all AND gates were replaced by NOT‑OR combinations (the only primitives available in redstone).  
6. **Vertical stacking** – The whole circuit for one digit was replicated above itself to drive the tens digit.  
7. **Redstone implementation** – Torches (NOT) and dust (OR) implement the final logic.

### The “Default‑On” Challenge
Redstone torches are **on by default**. This means the circuit tends to light segments when no input is active. To display **0** correctly, we designed the logic so that with no lever pulled, the segments that form a “0” light up. There is no “all‑off” state – 0 is the intended default.

---

## 🔌 Why Only NOT and OR?

Minecraft redstone provides two basic logic components:
- **Redstone torch** → NOT gate (output ON when input OFF).
- **Redstone dust** → OR gate (output ON if any input is ON).

AND gates are simulated using De Morgan’s law:  
`A AND B = NOT( (NOT A) OR (NOT B) )`  

All expressions in this project were converted to this NOT‑OR form. See [`circuit docs/AND to OR-NOT.md`](./circuit%20docs/AND%20to%20OR-NOT.md) for a detailed explanation.

---

## 📈 Project Evolution

This repository also contains two earlier (unoptimized) versions for comparison:
- **`first_attempt_single_display/`** – A single‑digit 0‑9 display with non‑minimized logic.
- **`second_attempt_double_display/`** – A two‑digit 00‑99 display using the same unoptimized logic.

These show the iterative improvement process and the importance of Boolean minimization when working with redstone.

---

## 🔢 Hexadecimal Extension

The folder **`hexadecimal_circuit/`** (inside `legacy_attempts/`) contains a complete theoretical design for a hexadecimal encoder (0‑9, A‑F). It includes truth tables, Karnaugh maps, minimized expressions, and circuit schematics. The design is fully worked out but was **not built in Minecraft** due to the excessive wiring complexity in 3D.

---

## 📊 Legacy Attempts vs Final (Optimised)

| Version | Status | Minimisation | Redstone Size | Latency | Playable |
|---------|--------|--------------|---------------|---------|----------|
| **Single digit 0‑9 (unoptimised)** | Working | ❌ Incorrect (redundant implicants) | Large | High | ✅ |
| **Double digit 00‑99 (unoptimised)** | Working | ❌ Same as above | Very large (100‑lever keypad) | High | ✅ |
| **Hexadecimal 0‑F (theoretical)** | Paper only | ✅ Optimal + gate sharing | Not built (impossible to wire compactly) | N/A | ❌ |
| **Final 00‑99 Display** | Working | ✅ Correctly minimised | Compact (vertical stacking) | Low | ✅ |

The final version uses the **same vertical layering** as the second attempt but with **correctly minimised Boolean expressions**, resulting in fewer gates, shorter signal paths, and a much cleaner redstone layout.

> 📖 Full details and “rough” documentation of the legacy attempts are available in the [`legacy_attempts/`](./legacy_attempts) folder.

---

## 🙏 Credits

- **Davide Ferigato** – Project design, redstone implementation, documentation.  
- **Roberto Tittoto** – Collaboration on the first Karnaugh maps (single‑digit unoptimised version).  
- Thanks to the Minecraft redstone community for inspiration.

---

## 📄 License

This project is open source and available under the **MIT License**. See the [LICENSE](./LICENSE) file for details.