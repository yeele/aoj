import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)
n, q = map(int, input().split())

ki = [[] for i in range(n + 1)]
for i in range(n - 1):
    a, b = map(int, input().split())
    ki[a].append(b)
    ki[b].append(a)
# print(ki)

cnt = [0] * (n + 1)
for i in range(q):
    p, x = map(int, input().split())
    cnt[p] += x

# print(cnt)
def d(y, parent):
    for i in ki[y]:
        if i == parent:
            continue
        cnt[i] += cnt[y]
        d(i, y)


d(1, -1)
print(*cnt[1:])