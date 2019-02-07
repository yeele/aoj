#-*- coding: utf-8 -*-
"""
http://elementsofprogramminginterviews.com/sample/epilight_python_new.pdf
"""

#   5
# 101
def rec2_this_one_works_too(n):
    if n > 0:
        rec(n-1)
        print("*", end="")

def rec(n):
    if n == 1:
        print("*", end="")
    else:
        print("*", end="")
        rec(n-1)


def print_stars(n):
    rec(n)
    print("\n-----------")

print_stars(1)
print_stars(10)

