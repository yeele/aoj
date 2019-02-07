#-*- coding: utf-8 -*-
"""
http://elementsofprogramminginterviews.com/sample/epilight_python_new.pdf
"""


def gcd(a, b, l):
    print("%sgcd(%s, %s)" % (" "*l, a, b))
    # base case
    if b == 0:
        return a
    else:
        l+=1
        return gcd(b, int(a%b), l)


print(gcd(24, 9, 0))
print(gcd(156, 36, 0))
