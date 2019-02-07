#-*- coding: utf-8 -*-
#one of the guy said , this question was asked during the interview.
#why merge sort over quick sort, when? pros/cons?
"""
順番は違うんだが、マージソートはアレイを使うので、要領を少し食うと言う印象です

"""
from sys import stdin, stdout
import queue
def show_pointer(S, i, j, p):
    print("----------------")
    for m in range(len(S)):
        print(m, end="")
    print("\n", end="")
    for m in range(len(S)+1):
        if m == i: print("i", end="")
        else: print(" ", end="")
    print("\n", end="")
    for m in range(len(S)+1):
        if m == j: print("j", end="")
        else: print(" ", end="")
    print("\n", end="")
    for s in S:
        print(s, end="")
    print("\n", end="")

    for m in range(len(S)+1):
        if m == p: print("p", end="")
        else: print(" ", end="")
    print("\n----------------")

def choose_pivot(S, i, j):
    # very right one, same as my reference
    return j

def swap(S, i, j):
    logging.debug("swap i:%s j:%s" % (i,j))
    tmp = S[i]
    S[i] = S[j]
    S[j] = tmp

# i: first index
# j: last index
def quick_sort(S, i, j):
    start = i
    end = j
    # choose a pivot
    if i == j: return
    if i > j:
        logging.error("unexpected")
        return
    pivot = choose_pivot(S, i, j)
    # pointer i to the most left
    i = i
    # pointer j to the most right
    j -= 1
    # move i until S[i] is bigger

    c=0
    while i < j:
        logging.error("miso1 %s" % c)
        show_pointer(S, i, j, pivot)
        while True:
            if S[i] > S[pivot]:break
            if i == pivot:
                # pivot is largest
                break
            i+=1
        while True:
            if i > j: break # 左マーカーに追い越されている
            if S[j] < S[pivot]:break
            if i == j: break
            j-=1

        if i < j: swap(S, i, j)
        elif i == j: swap(S, i, pivot)
        c+=1

    quick_sort(S, start, pivot-1)
    quick_sort(S, pivot+1, end)



def sol(x):
    quick_sort(x, 0, len(x)-1)
    return x


def test():
    #x = [6, 4, 3, 7, 5, 1, 2]
    #x = [19, 3, 1, 91,22, 20, 16, 7,8, 9,6]
    x = [3, 5, 8, 1, 2, 9 ,4, 7, 6]
    x = [7, 3, 1, 9, 8, 6, 2, 4, 5]
    ret = sol(x)
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
    import logging
    logging.basicConfig(level=logging.DEBUG, format="%(message)s")
    #main()
    test()


