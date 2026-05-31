#!/usr/bin/env python3
"""Generate a truth table CSV (with ; delimiter) from the minimised expressions.
   Rows 0-9: digit number; rows 10-15: 'x' in first column, segments computed.
   Output file: generated_truth_table.csv (saved in the current directory).
"""

import csv
from simulate_decoder import segment_a, segment_b, segment_c, segment_d, segment_e, segment_f, segment_g

def bcd_to_bits(n):
    """Convert 4-bit number n (0-15) to (A,B,C,D) where A is MSB."""
    return ((n >> 3) & 1, (n >> 2) & 1, (n >> 1) & 1, n & 1)

def main():
    with open("generated_truth_table.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f, delimiter=';')
        writer.writerow(["Case", "A", "B", "C", "D", "a", "b", "c", "d", "e", "f", "g"])
        for n in range(16):
            A, B, C, D = bcd_to_bits(n)
            a = int(segment_a(A, B, C, D))
            b = int(segment_b(A, B, C, D))
            c = int(segment_c(A, B, C, D))
            d = int(segment_d(A, B, C, D))
            e = int(segment_e(A, B, C, D))
            f = int(segment_f(A, B, C, D))
            g = int(segment_g(A, B, C, D))
            if n <= 9:
                case = str(n)
            else:
                case = "x"
            writer.writerow([case, A, B, C, D, a, b, c, d, e, f, g])
    print("Generated generated_truth_table.csv (semicolon-separated)")

if __name__ == "__main__":
    main()
