#-*- coding: utf-8 -*-
#https://www.geeksforgeeks.org/find-a-triplet-that-sum-to-a-given-value/
#https://www.geeksforgeeks.org/find-triplets-array-whose-sum-equal-zero/

from sys import stdin, stdout
import copy
def rec(S, i, n, sets, t):
    print("(S:%s, i:%s, n:%s, sets:%s, t:%s)" % (S, i, n, sets, t))
    if i >= len(S)+1: return []
    if n == 3:
        if sum(sets) == t:
            return sets
        else: return []
    elif n > 3:
        return []
    else:
        sets1 = rec(S, i+1, n, copy.copy(sets), t)
        if i < len(S): sets.append(S[i])
        sets2 = rec(S, i+1, n+1, copy.copy(sets), t)
        if sets1 is not None:
            print("ans:%s" % sets1)
        if sets2 is not None:
            print("ans:%s" % sets2)
        return "%s:%s" % (sets1, sets2)

def sol(S, t):
    print("sol(%s, %s)" % (S, t))
    return rec(S, 0, 0, [], t)

def test():
    x = [0, -1, 2, -3, 1]
    t = 0
    ret = sol(x, t)
    stdout.write("%s\n" % str(ret))

def main():
    n_ts = int(stdin.readline())
    for i in range(n_ts):
        n = int(stdin.readline())
        S = [int(x) for x in stdin.readline().split()]
        ret = sol(S)
        stdout.write("%s\n" % str(ret))

# call the main method
if __name__ == "__main__":
    #main()
    test()


