#-*- coding: utf-8 -*-


def gcd(m, n):
    r = m % n
    return gcd(n, r) if r else n
def lcm(x, y):
    return (x * y) // gcd(x, y)

def sol(a, b):
    return (a * b) // gcd(a, b)


a, b = list(map(int, input().split()))
print(sol(a, b))






