#!/user/bin/python3
# SPDX-FileCopyrightText: 2023 Naoki Kobayashi
# SPDX-License-Identifier: BSD-3-Clause

import sys

x = 0.0
for n in sys.argv[1:]:
    b = float(n)
    x += b * 2
print(x)
