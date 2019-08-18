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


class TreeNode:
    def __init__(self):
        self.val = 0
        self.vertex = []

def make_trees(n, A, B):
    trees = []
    for i in range(n):
        trees.append(TreeNode())
    for i in range(len(A)):
        a = A[i]-1
        b = B[i]-1
        trees[a].vertex.append(b)
    return trees

def dfs(node: TreeNode, x: int, trees):
    if node:
        node.val += x
        for i in node.vertex:
            dfs(trees[i], x, trees)


def sol(n, q, A, B, P, X):
    trees = make_trees(n, A, B)
    for i in range(len(P)):
        p = P[i]-1
        x = X[i]
        t = trees[p]
        # dfs, give point x
        dfs(t, x, trees)
    #
    return " ".join([str(t.val)  for t in trees])
    #return n, q, A, B, P, X



do_submit = True
do_submit = False

def input_parse(input_str):
    lines = [x.strip() for x in input_str.split("\n") if x.strip()]
    parsed_lines = [list(map(str, line.split())) for line in lines]
    print(parsed_lines)
    n = int(parsed_lines[0][0])
    q = int(parsed_lines[0][1])
    A = []
    B = []
    P = []
    X = []
    for i in range(1, n-1+1):
        a = int(parsed_lines[i][0])
        b = int(parsed_lines[i][1])
        A.append(a)
        B.append(b)
    for i in range(n, 1+n+q-1):
        p = int(parsed_lines[i][0])
        x = int(parsed_lines[i][1])
        P.append(p)
        X.append(x)

    # S = parsed_lines[1][0]
    # return n, k, S
    return n, q, A, B, P, X


if not do_submit:
    n, q, A, B, P, X = input_parse("""
    4 3
    1 2
    2 3
    2 4
    2 10
    1 100
    3 1
    """)
    print(sol(n, q, A, B, P, X))

    n, q, A, B, P, X = input_parse("""
        6 2
        1 2
        1 3
        2 4
        3 6
        2 5
        1 10
        1 10
    """)
    print(sol(n, q, A, B, P, X))

else:
    # n = int(input().strip())
    # q = int(input().strip())
    n, q = list(map(int, input().split()))
    A = []
    B = []
    P = []
    X = []
    for i in range(n-1):
        a, b = list(map(int, input().split()))
        # a = int(input().strip())
        # b = int(input().strip())
        A.append(a)
        B.append(b)
    for i in range(q):
        p, x = list(map(int, input().split()))
        # p = int(input().strip())
        # x = int(input().strip())
        P.append(p)
        X.append(x)
    print(sol(n, q, A, B, P, X))

