#-*- coding: utf-8 -*-
#https://practice.geeksforgeeks.org/problems/longest-increasing-subsequence/0

from sys import stdin, stdout
def lis(S):
    sz = len(S)
    dp = [1] * sz
    ac = [ str(x) for x in S]
    for i in range(1, sz):
        for j in range(i):
            if S[j] < S[i]:
                if dp[j]+1 > dp[i]:
                    dp[i] = dp[j]+1
                    ac[i] += "," + str(S[j])
    #print(dp)
    #print(ac)
    return max(dp)




def test():
    S = [10, 22, 9, 33, 21, 50, 41, 60, 80]
    #S = [int(x) for x in "0 8 4 12 2 10 6 14 1 9 5 13 3 11 7 15".split()]
    ret = lis(S)
    stdout.write("%s\n" % str(ret))

def main():
    n_ts = int(stdin.readline())
    for i in range(n_ts):
        n = int(stdin.readline())
        S = [int(x) for x in stdin.readline().split()]
        ret = lis(S)
        stdout.write("%s\n" % str(ret))

# call the main method
if __name__ == "__main__":
    #main()
    test()


