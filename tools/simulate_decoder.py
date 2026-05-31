#!/usr/bin/env python3
"""Simulate the BCD to 7-segment decoder for digits 0-9 using minimised expressions."""

import sys

def segment_a(A, B, C, D):
    # a = A + C + (NOT B AND NOT D) + (B AND D)
    return A or C or (not B and not D) or (B and D)

def segment_b(A, B, C, D):
    # b = A + B + (NOT C AND NOT D)
    return A or B or (not C and not D)

def segment_c(A, B, C, D):
    # c = NOT B + (C AND D) + (NOT C AND NOT D)
    return (not B) or (C and D) or (not C and not D)

def segment_d(A, B, C, D):
    # d = A + (NOT B AND C) + (B AND NOT D) + (B AND NOT C)
    return A or (not B and C) or (B and not D) or (B and not C)

def segment_e(A, B, C, D):
    # e = (NOT B AND NOT D) + (C AND NOT D)
    return (not B and not D) or (C and not D)

def segment_f(A, B, C, D):
    # f = NOT C + B + D
    return (not C) or B or D

def segment_g(A, B, C, D):
    # g = A + (NOT B AND NOT D) + (NOT B AND C) + (C AND NOT D) + (B AND NOT C AND D)
    return A or (not B and not D) or (not B and C) or (C and not D) or (B and not C and D)

def digit_to_bcd(d):
    """Return (A,B,C,D) bits for decimal digit d (0-9). A is MSB."""
    if not 0 <= d <= 9:
        raise ValueError("Digit must be 0-9")
    return ((d >> 3) & 1, (d >> 2) & 1, (d >> 1) & 1, d & 1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python simulate_decoder.py <digit>")
        sys.exit(1)
    d = int(sys.argv[1])
    A, B, C, D = digit_to_bcd(d)
    a = segment_a(A, B, C, D)
    b = segment_b(A, B, C, D)
    c = segment_c(A, B, C, D)
    d_out = segment_d(A, B, C, D)
    e = segment_e(A, B, C, D)
    f = segment_f(A, B, C, D)
    g = segment_g(A, B, C, D)
    print(f"Digit {d} (BCD {A}{B}{C}{D})")
    print(f"Segments: a={int(a)} b={int(b)} c={int(c)} d={int(d_out)} e={int(e)} f={int(f)} g={int(g)}")
