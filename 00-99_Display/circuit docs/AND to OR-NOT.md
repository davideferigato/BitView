# Boolean Functions — De Morgan's Law

> In Minecraft's Redstone, AND gates cannot be built natively. Only OR and NOT are available.

---

a = C + A + \bar{B}\bar{D} + B D --> A + C + \overline{B + D} + \overline{\bar{B} + \bar{D}}

b = A + B + \bar{C}\bar{D} --> A + B + \overline{C + D}

c = \bar{B} + C D + \bar{C}\bar{D} --> \bar{B} + \overline{\bar{C} + \bar{D}} + \overline{C + D}

d = A + \bar{B} C + B \bar{D} + B \bar{C} --> A + \overline{B + \bar{C}} + \overline{\bar{B} + D} + \overline{\bar{B} + C}

e = \bar{B}\bar{D} + C\bar{D} --> \overline{B + D} + \overline{\bar{C} + D}

f = \bar{C} + B + D --> \bar{C} + B + D

g = A + \bar{B}\bar{D} + \bar{B}C + C\bar{D} + B\bar{C}D --> A + \overline{B + D} + \overline{B + \bar{C}} + \overline{\bar{C} + D} + \overline{\bar{B} + C + \bar{D}}