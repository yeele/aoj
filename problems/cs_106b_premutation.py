#-*- coding: utf-8 -*-
#https://www.youtube.com/watch?v=78t_yHuGg-0&t=600s
from sys import stdout
import copy
def sol(S, chosen=""):
    #print("miso1: S:%s, chosen:%s, len(S):%s" % (S, chosen, len(S)))
    if S == "":
        print(chosen)
    else:
        sz = len(S)
        for i in range(sz):
            # choose
            #print("miso2: S:%s, chosen:%s, i:%s, len(S):%s" % (S, chosen, i, len(S)))
            c = S[i]
            idx = S.find(c)
            preserved = S
            S = S.replace(c, '', 1)
            chosen+=c

            # permutate
            sol(S, chosen)

            # un-choose
            #print("S:%s, idx:%s, S[0:idx]:%s+c:%s+S[idx+1:]:%s, chosen:%s" % (S, idx, S[0:idx], c, S[idx+1:], chosen))
            S = preserved
            chosen = chosen[0:-1]


def test():
    x = "MARTY"
    ret = sol(x, "")
    stdout.write("%s\n" % str(ret))


# call the main method
if __name__ == "__main__":
    import logging
    logging.basicConfig(level=logging.DEBUG, format="%(message)s")
    #main()
    test()


