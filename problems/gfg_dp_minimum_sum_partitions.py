#code
#https://practice.geeksforgeeks.org/problems/longest-common-subsequence/0/?ref=self
from sys import stdin, stdout
from collections import defaultdict
dp = {}
def rec_bu(S, i, subttl, ttl):
    print("S:%s, i:%s, subttl:%s, ttl:%s" % (S, i, subttl, ttl))
    if i == len(S)-1:
        sumA = subttl
        sumB = ttl-sumA
        diff = abs(sumA-sumB)
        return diff

    return min(
        rec(S, i + 1, subttl, ttl),
        rec(S, i + 1, subttl + S[i], ttl)
    )

def rec_topdown(S, i, subttl, ttl):
    #print("S:%s, i:%s, subttl:%s, ttl:%s" % (S, i, subttl, ttl))
    if (subttl) in dp:
        #print("hit:dp[i:%s, subttl:%s] is %s" % (i, subttl, dp[subttl]))
        return dp[subttl]

    if i == len(S)-1:
        sumA = subttl
        sumB = ttl-sumA
        diff = abs(sumA-sumB)
        dp[subttl] = diff
        return dp[subttl]

    mini = min(
        rec(S, i + 1, subttl, ttl),
        rec(S, i + 1, subttl + S[i], ttl)
    )
    #dp[subttl] = mini
    #return dp[subttl]
    return mini

def rec(S, i, subttl, ttl):
    #print("S:%s, i:%s, subttl:%s, ttl:%s" % (S, i, subttl, ttl))
    if i == len(S)-1:
        sumA = subttl
        sumB = ttl-sumA
        diff = abs(sumA-sumB)
        return diff

    return min(
        rec(S, i + 1, subttl, ttl),
        rec(S, i + 1, subttl + S[i], ttl)
    )

def sol(S):
    ttl = sum(S)
    # S, how many in setA, sum of setA, sum of given S
    #mini = rec(S, 0, 0, ttl)
    mini = rec_topdown(S, 0, 0, ttl)
    return mini

def test():
    S = [1, 6, 5, 11]
    S = [36, 7, 46, 40]
    ret = sol(S)
    stdout.write("%s\n" % str(ret))

def main():
    n_ts = int(stdin.readline())
    for i in range(n_ts):
        n = int(stdin.readline().strip())
        S = [ int(x) for x in stdin.readline().strip().split()]
        ret = sol(S)
        stdout.write("%s\n" % str(ret))

# call the main method
if __name__ == "__main__":
    #main()
    test()