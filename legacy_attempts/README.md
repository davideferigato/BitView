# Legacy Attempts – The Road to BitView

This folder contains the early, unoptimized (or only partially implemented) versions of the display projects. They are preserved here to show the **learning process**, the evolution of the design, and the importance of correct Boolean minimization when working with Minecraft redstone.

All these attempts were essential stepping stones toward the final optimized `00-99_Display` (the main BitView world).

---

## 1. First Attempt – Single Digit 0‑9 Display (Unoptimized)

**Folder:** `first_attempt_single_display/`

### Input
- **10 levers** (one for each decimal digit 0–9). No binary encoding – each lever directly selects a digit.

### Logic Design Flaw
- The Karnaugh maps were **not minimized correctly**.  
- The resulting Boolean expressions contained redundant implicants (the set of prime implicants was not minimal).  
- The circuit works **perfectly** (all digits 0–9 are displayed correctly), but it is **inefficient**:
  - More logic gates than necessary.
  - Longer signal propagation delays → segments light up more slowly.

### Documentation
- `first k-maps.pdf` – Karnaugh maps drawn with the help of a university colleague (Roberto Tittoto). These maps were correctly built but **not optimally minimized**.
- `wrong optimized logic circuit.jpg` – The logic circuit derived from the non‑minimal expressions.

### State
- Fully playable Minecraft world (`BitView_0-9_Unoptimized`).  
- No visual errors – only performance and compactness issues.

### Didactic Value
- First approach to implementing Boolean logic in Minecraft.  
- Demonstrated that **correct minimization is not trivial** and directly affects circuit speed and size.

---

## 2. Second Attempt – Double Digit 00‑99 Display (Unoptimized)

**Folder:** `second_attempt_double_display/`

### Architecture
- Direct replication of the first (unoptimized) single‑digit module:  
  Two identical layers (tens and units) stacked vertically, exactly as later used in the final optimized version.
- The idea was to create a **layered system** to support multiple digits (tens, hundreds, etc.).

### Input
- A **100‑lever keypad** (00 to 99) – each lever directly selects a two‑digit number.  
- In the physical Minecraft build, the keypad was only partially connected because routing 100 independent signals to the two digit modules became **too complex and space‑consuming**.  
- Despite this, the world **is fully playable** and the display shows the correct number for any lever you pull (the keypad is functional but not compact).

### Problems (Beyond Non‑Minimization)
- **Space explosion** – connecting the 100‑lever keypad to the two digit modules required enormous wiring, making the build impractical for the intended layout.  
- **Latency** – same as first attempt: non‑minimized expressions caused slower signal propagation (excessive use of repeaters).  
- No communication needed between the tens and units layers – they are independent.

### Functionality
- The world **works correctly** (all numbers 00–99 are displayed without errors), as shown in the included screenshots and video (`test 00.png`, `test 42.png`, `test 99.png`, `record test.mp4`).

### Documentation
- `dec old double display ideas.pdf` – Early sketches and design notes.
- Screenshots and video demonstrating the working world.

### Differences from the Final Optimized Version
- **Identical layout** (vertical layering, side‑by‑side displays).  
- **Only the Boolean expressions** were later minimized correctly, which drastically reduced the number of gates, repeaters, and overall size.

### State
- **Fully playable** Minecraft world (`BitView_00-99_Unoptimized`).  
- Preserved to show the original unoptimized implementation.

---

## 3. Third Attempt – Hexadecimal Display (0‑9, A‑F) – Theoretical Only

**Folder:** `hexadecimal_circuit/` (inside `legacy_attempts/` – note: this is **not** a Minecraft world, only a logical design)

### Scope
- Extend the 7‑segment decoder to support **16 characters** (0–9, A, B, C, D, E, F).  
- The design was carried out **on paper** (truth tables, Karnaugh maps, minimized expressions, gate‑sharing optimization).  
- **Never implemented in Minecraft** because the physical redstone routing would be impossible to keep compact.

### Key Features of the Design
- **Very high level of minimization** – not only minimal AND‑OR expressions, but also **gate reuse** across different outputs to reduce the total number of logic gates.  
- The resulting circuit is **optimal on paper** but **impossible to build in a compact way in Minecraft** due to the 3D wiring constraints (redstone dust connects to adjacent blocks, making complex interconnections unmanageable).

### Display Limitations
- A 7‑segment display cannot perfectly show all hexadecimal letters.  
- **Solution adopted in the design:**  
  - Use **lowercase** for `b` and `d` to distinguish them from `8` and `0`.  
  - All other letters remain uppercase.

### Documentation (Complete)
- `truth table.csv` – Full truth table for 4 inputs → 7 segments (16 rows).
- `karnaugh maps.pdf` + `karnaugh maps.tex` – K‑maps for each segment.
- `logic circuit.drawio` + `logic circuit.jpg` – Schematic of the minimized and gate‑shared circuit.
- All files are **clean and well‑organized** (not “rough” – this part was done carefully).

### Why It’s a “Legacy Attempt”
- It represents the **natural evolution** of the final optimized decimal display toward a more powerful hexadecimal decoder.  
- It shows the **limit of practical redstone implementation** – even a perfectly minimized logic design can become impossible to wire in Minecraft’s 3D block grid.

### Didactic Value
- Demonstrates the use of **don’t‑care conditions** (inputs 10–15 were unused in decimal, but become valid in hexadecimal).  
- Shows how **aggressive minimization and gate sharing** can reduce complexity on paper, but physical constraints (Minecraft redstone) may still prevent a build.  
- Highlights the difference between **logical minimisation** and **physical layout feasibility**.

---

## Summary – The Learning Path

| Attempt | Status | Main Issue | Value for the Final Project |
|---------|--------|------------|------------------------------|
| Single digit 0‑9 | Working, unoptimized | Non‑minimal expressions → slow, large | Showed that minimization matters |
| Double digit 00‑99 | Working, unoptimized | Same non‑minimization + keypad wiring complexity | Validated the vertical layering concept |
| Hexadecimal 0‑F | Theoretical only | Physically impossible to route in Minecraft | Demonstrated the limits of redstone and the power of don’t‑cares |

All three attempts were **essential** to develop the final optimized `BitView/00-99_Display`. The rough, unpolished documentation (especially for the first two) is intentionally kept as‑is to reflect the **real, messy process of learning and iterating**.

> *“These attempts taught me that a correct Boolean expression is not enough – you also need to minimise it properly, and even then, Minecraft’s redstone may still say no.”*