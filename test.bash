#!/bin/bash
# SPDX-FileCopyrightText: 2023 Naoki Kobayashi

x=$(./plus_b.py 1 3 5)

[ "${x}" = 18.0 ]
