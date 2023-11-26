#!/bin/bash
# © 2023 Naoki Kobayashi
import sys

x = 0.0
for n in sys.argv[1:]:
    b = float(n)
    x += b * 2
print(x)
