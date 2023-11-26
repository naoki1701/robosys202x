#!/bin/bash
# © 2023 Naoki Kobayashi

out=$(python3 plus_b.py 1 3 5)

[ "${out}" = 18.0 ]
