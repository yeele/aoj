
do_submit = True

# if not do_submit:
#     n, q, A, B, P, X = input_parse("""
#     4 3
#     1 2
#     2 3
#     2 4
#     2 10
#     1 100
#     3 1
#     """)
#     print(sol(n, q, A, B, P, X))
#
#     n, q, A, B, P, X = input_parse("""
#         6 2
#         1 2
#         1 3
#         2 4
#         3 6
#         2 5
#         1 10
#         1 10
#     """)
#     print(sol(n, q, A, B, P, X))
#
#     n, q, A, B, P, X = input_parse("""
#         10 5
#         1 2
#         1 3
#         1 4
#         2 5
#         2 6
#         3 7
#         4 8
#         4 9
#         7 10
#         7 3
#         3 100
#         1 2
#         5 10
#         4 11
#     """)
#     print(sol(n, q, A, B, P, X))
import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)
n, q = map(int, input().split())

trees = [ [] for i in range(n+1) ]
for i in range(n-1):
    a, b = map(int, input().split())
    trees[a].append(b)
    trees[b].append(a)

values = [ 0 for i in range(n+1) ]
for i in range(q):
    p, x = map(int, input().split())
    values[p] += x
#print(values)

def dfs2(i, parent):
    for j in trees[i]:
        if j == parent: continue
        values[j] += values[i]
        dfs2(j, i)

dfs2(1, -1)
print(*values[1:])

