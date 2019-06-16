#-*- coding: utf-8
#  -*-
"""
oj dl https://atcoder.jp/contests/abc116/tasks/abc116_d -d test-d
oj test -d test-d -c "python abc116d.py"
oj test -d test-d -c "python abc116d.py" test-d/sample-3.in
"""
from collections import defaultdict
import sys
import math
from datetime import datetime

class Room():
    def __init__(self, depth, width):
        self.depth = depth
        self.width = width

    @classmethod
    def empty(cls):
        return Room(0, 0)
    def __str__(self):
        return "d:%d, w:%d" % (self.depth, self.width)


def sol(h, w, S):
    pre_room = None
    dp = [[Room(0,0)] * (w+1) for i in range(h+1)]
    print(dp)
    for i, s in enumerate(S):
        for j, room in s:
            print(r)
    return h, w, S


do_submit = True
do_submit = False

def input_parse(input_str):
    lines = [x.strip() for x in input_str.split("\n") if x.strip()]
    parsed_lines = [list(map(str, line.split())) for line in lines]
    #print(parsed_lines)
    h = int(parsed_lines[0][0])
    w = int(parsed_lines[0][1])
    #print(n, m)
    S = []
    for i in range(1, h+1):
        S.append(parsed_lines[i][0])
    print(h, w, S)

    # W = [int(x) for x in parsed_lines[1]]
    # k = int(parsed_lines[0][1])
    # S = parsed_lines[1][0]
    # return n, k, S
    return h, w, S


if not do_submit:
    h, w, S = input_parse("""
    4 6
    #..#..
    .....#
    ....#.
    #.#...
    """)
    print(sol(h, w, S))



else:
    #n = int(input())
    h, w = list(map(int, input().split()))
    S = []
    for i in range(h):
        S.append(input().strip())
    # print(sol(n, k, S))
    #S = input().strip()
    # S = input().strip()
    print(sol(h, w, S))

