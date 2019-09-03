#-*- coding: utf-8 -*-
def sol(n):
    if n <= 0: return 0
    if n == 1:
        return 0
    if n == 2:
        return 1
    x = n - 1
    if x % 2 == 0: # even
        return ((x + 1) * int(x/2))
    else: # odd
        return ((x + 1) * int(x/2)) + int((x+1)/2)



n = int(input().strip())
print (sol(n))


