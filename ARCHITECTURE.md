# Architecture of BitView

## Overview
BitView implements a **two‑digit decimal display (00‑99)** in Minecraft redstone using only **NOT and OR gates**. The design follows a systematic digital logic methodology.

## High‑level structure
```
+----------------+     +-----------------+     +------------------+
| Keypad (levers)|                 +-----------------+     +------------------+
```

## Layering (vertical)
- **Units layer** (bottom): circuit for the rightmost digit.
- **Tens layer** (above): identical circuit for the leftmost digit.
- The two layers are physically stacked vertically to save horizontal space.
- **Displays** are placed side by side (tens left, units right) for natural reading.

## Signal flow (per digit)
1. **Lever block** (3×3, digits 1‑9) – each lever corresponds to one decimal digit.
2. **Encoder** – converts the lever input into a 4‑bit Binary Coded Decimal (BCD) value (0‑9).
3. **Decoder** – 4 inputs (A,B,C,D) → 7 outputs (segments a‑g).
   - The decoder is built from minimised Boolean expressions derived from **Karnaugh maps**.
   - Original expressions were in **AND‑OR** form.
   - Using **De Morgan’s law**, each AND gate is replaced by `NOT((NOT A) OR (NOT B))`.
4. **Redstone implementation**:
   - NOT gate = redstone torch.
   - OR gate = redstone dust (wire).
5. **7‑segment display** – lights the appropriate segments.

## Why only NOT and OR?
Minecraft redstone provides:
- **Torch**: NOT (output ON when input OFF).
- **Dust**: OR (output ON if any input is ON).
No native AND gate. Therefore all Boolean expressions must be converted to NOT‑OR form. This is done systematically using De Morgan:

```
A AND B = NOT( (NOT A) OR (NOT B) )
```

## Handling the “default‑on” issue
Redstone torches are ON by default. This means when no lever is pulled, the circuit tends to output ON. To correctly display **0**, the logic was designed so that with all levers off, the segments that form a “0” light up. There is no “all‑off” state – 0 is the intended default.

## Quantitative improvements (compared to legacy)
See the **Quantitative Results** section in the main README for exact numbers. In summary, the optimised version reduces gate count by approximately `[TODO: %]` and eliminates unnecessary repeaters, lowering latency.

## Legacy versions
- `first_attempt_single_display/`: unoptimised 0‑9 digit.
- `second_attempt_double_display/`: unoptimised 00‑99 using the same flawed minimization.

## Hexadecimal extension (theoretical)
- Designed but not built in Minecraft.
- Uses the same architecture but with a 4‑input to 7‑segment truth table for 0‑9 and A‑F.
- Includes gate sharing to minimise logic.
- Not built due to 3D wiring complexity in redstone.

## Future possibilities
- Adding a hundreds digit (another layer).
- Implementing the hexadecimal decoder in a larger world.
- Writing a Python simulator that mirrors the redstone logic.

