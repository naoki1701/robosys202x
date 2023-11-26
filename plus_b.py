#!/bin/bash
# © 2023 Naoki Kobayashi
import sys

x = 0.0
for n in sys.argv[1:]:
    a = float(n)
    x += a * 2
print(x)
