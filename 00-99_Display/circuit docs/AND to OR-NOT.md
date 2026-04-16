# Boolean Functions — De Morgan's Law

> In Minecraft's Redstone, AND gates cannot be built natively. Only OR and NOT are available.

---

a = C + A + NOT(B)NOT(D) + B D --> A + C + NOT(B + D) + NOT(NOT(B) + NOT(D))

b = A + B + NOT(C)NOT(D) --> A + B + NOT(C + D)

c = NOT(B) + C D + NOT(C)NOT(D) --> NOT(B) + NOT(NOT(C) + NOT(D)) + NOT(C + D)

d = A + NOT(B) C + B NOT(D) + B NOT(C) --> A + NOT(B + NOT(C)) + NOT(NOT(B) + D) + NOT(NOT(B) + C)

e = NOT(B)NOT(D) + C NOT(D) --> NOT(B + D) + NOT(NOT(C) + D)

f = NOT(C) + B + D --> NOT(C) + B + D

g = A + NOT(B)NOT(D) + NOT(B)C + C NOT(D) + B NOT(C) D --> A + NOT(B + D) + NOT(B + NOT(C)) + NOT(NOT(C) + D) + NOT(NOT(B) + C + NOT(D))