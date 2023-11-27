#!/bin/bash
# SPDX-FileCopyrightText: 2023 Naoki Kobayashi

out=$(./plus_b.py 1 3 5)

[ "${out}" = 18.0 ]
