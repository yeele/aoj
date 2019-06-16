#-*- coding: utf-8 -*-
"""
https://github.com/kmyk/online-judge-tools
"""

from collections import defaultdict
import sys


import math
def sol(a, b, c):
    #return math.sqrt(a**2+b**2)
    return int(a*b/2)




testManual = False
submitVersion = True
def input_parse(input_str):
    lines = [x.strip() for x in input_str.split("\n") if x.strip()]
    parsed_lines = [list(map(int, line.split())) for line in lines]
    a, b, c = parsed_lines[0]
    #A = parsed_lines[1]
    #print(n, m, A)
    #return (n, m, A)
    return a, b, c
if testManual:
    n, m, A = input_parse("""
    45 28 53
    """)
    print(sol(n, m, A))
if submitVersion:
    #n = int(input().strip())
    #n, k = map(int, input().split())
    ##S =list( map(int, "1 6 3".split()))
    #print("%s %s %s %s" % (type(n), type(k), n, k))
    a, b, c =list( map(int, input().split()))
    print(sol(a, b, c))


