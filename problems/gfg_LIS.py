#-*- coding: utf-8 -*-
#https://practice.geeksforgeeks.org/problems/longest-increasing-subsequence/0

"""
Input
1
16
0 8 4 12 2 10 6 14 1 9 5 13 3 11 7 15
Output
6
"""
#code
from sys import stdin, stdout
def lis(S):
    sz = len(S)
    dp = [[0] * sz for _ in range(sz)]
    for i in range(sz):
        #print("\n%s:" % i, end="")
        seq = 1
        m = 0
        for j in range(i, sz):
            #print(j, end=" ")
            cur = S[j]
            if cur > m:
                m = max(m, cur)
                seq += 1
            dp[i][j] = max(seq, dp[i-1][j])
    for row in dp:
        print(row)
    return dp[-1][-1]




def test():
    S = [10, 22, 9, 33, 21, 50, 41, 60, 80]
    S = [int(x) for x in "0 8 4 12 2 10 6 14 1 9 5 13 3 11 7 15".split()]
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


