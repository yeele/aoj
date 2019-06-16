#-*- coding: utf-8 -*-
"""
"""

from collections import defaultdict
import sys

import math


def sol(a, b, c):
    return int(a * b / 2)


do_submit = True


def input_parse(input_str):
    lines = [x.strip() for x in input_str.split("\n") if x.strip()]
    parsed_lines = [list(map(int, line.split())) for line in lines]
    a, b, c = parsed_lines[0]
    return a, b, c


if not do_submit:
    a, b, c = input_parse("""
    45 28 53
    """)
    print(sol(a, b, c))
else:
    a, b, c = list(map(int, input().split()))
    print(sol(a, b, c))

