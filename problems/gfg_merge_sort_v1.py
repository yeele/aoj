#-*- coding: utf-8 -*-
#one of the guy said , this question was asked during the interview.
#why merge sort over quick sort, when? pros/cons?

from sys import stdin, stdout
import queue


def merge_sort(S):
    mid = int((len(S)-1)/2)
    if len(S) <= 1: return S
    else:
        a = merge_sort(S[0:mid + 1])
        b = merge_sort(S[mid + 1:])
        c = []
        while a or b:
            if a and b:
                if a[0] <b[0]: c.append(a.pop(0))
                else: c.append(b.pop(0))
            elif a:c.append(a.pop(0))
            else: c.append(b.pop(0))
        return c

def merge_sort_verbose(S):
    mid = int((len(S)-1)/2)
    print("merge_sort(%s) mid:%s"%(S,mid))
    if len(S) <= 1:
        # finish dividing
        print("miso1")
        return S
    else:
        a = merge_sort(S[0:mid + 1])
        print("a:%s"%a)
        b = merge_sort(S[mid + 1:]) if len(S)>1 else merge_sort([])
        print("b:%s"%b)
        c = []
        while a or b:
            if a and b:
                if a[0] <b[0]: c.append(a.pop(0))
                else: c.append(b.pop(0))
            elif a:c.append(a.pop(0))
            else: c.append(b.pop(0))
        print("c:%s"%c)
        return c


def sol(x):
    sorted_x = merge_sort(x)
    return sorted_x


def test():
    x = [6, 4, 3, 7, 5, 1, 2]
    x = [19, 3, 1, 91,22, 20, 16, 7,8, 9,6]
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
    #main()
    test()


