#-*- coding: utf-8 -*-
"""
http://elementsofprogramminginterviews.com/sample/epilight_python_new.pdf
"""

#   5
# 101
def rec(n):
    if n < 0:
        print('-', end="")
        rec(-n)
    elif n < 2:
        print("miso1")
        print(n, end="")
    else:
        print("miso2")
        least_d = 1 & n
        rest_d = n >> 1
        #print("least_d:%s rest_d:%s" % (least_d, rest_d))
        rec(rest_d)
        print(least_d, end="")



def print_binary(n):
    rec(n)
    print("\n-----------")

print_binary(1)
print_binary(2)
print_binary(3)
print_binary(15)
print_binary(43)
print_binary(-500)

