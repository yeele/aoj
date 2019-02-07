#-*- coding: utf-8 -*-
#one of the guy said , this question was asked during the interview.
#https://www.geeksforgeeks.org/google-interview-experience-set-7-software-engineering-intern/

from sys import stdin, stdout
import queue


def sol2(x):
    if x < 2: return 0
    else:  return 1+sol(int(x/2))

def sol(x):
    q = queue.Queue()
    while x > 0:
        md = x % 2
        nx = int(x / 2)
        q.put(md)
        x = nx
    while not q.empty():
        print(q.get())



def test():
    x = 146
    x = 4
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


