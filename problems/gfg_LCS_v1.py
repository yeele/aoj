#code
#https://practice.geeksforgeeks.org/problems/longest-common-subsequence/0/?ref=self
from sys import stdin, stdout
def lcs(a, b):
    dp = [[0] * (len(b)+1) for _ in range((len(a)+1))]
    for i in range(len(a)+1):
        for j in range(len(b)+1):
            if i == 0 or j == 0: dp[i][j] = 0
            elif a[i-1] == b[j-1]:
                #dp[i][j] = max(dp[i][j-1], dp[i-1][j]) + 1
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i][j-1], dp[i-1][j])
    return dp[-1][-1]


def lcs_doesnt_work(a, b):
    """
    初期化をちょっとはっ背負ってもいけるかな、と思いきや
    テストケースで落ちるパターンが！
    """
    dp = [[0] * len(b) for _ in range(len(a))]
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] == b[j]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i][j-1], dp[i-1][j])
    return dp[-1][-1]

def lcs(X , Y):
    # find the length of the strings
    m = len(X)
    n = len(Y)
    L = [[None]*(n+1) for i in range(m+1)]

    """Following steps build L[m+1][n+1] in bottom up fashion 
    Note: L[i][j] contains length of LCS of X[0..i-1] 
    and Y[0..j-1]"""
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0 :
                L[i][j] = 0
            elif X[i-1] == Y[j-1]:
                L[i][j] = L[i-1][j-1]+1
            else:
                L[i][j] = max(L[i-1][j] , L[i][j-1])

            # L[m][n] contains the length of LCS of X[0..n-1] & Y[0..m-1]
    return L[m][n]
#end of function lcs

def test():
    a = "ABCDGH"
    b = "AEDFHR"
    ret = lcs(a, b)
    stdout.write("%s\n" % str(ret))

def main():
    """
2
6 6
ABCDGH
AEDFHR
3 2
ABC
AC
    """
    n_ts = int(stdin.readline())
    for i in range(n_ts):
        (u, v) = stdin.readline().strip().split()
        a = stdin.readline().strip()
        b = stdin.readline().strip()
        ret = lcs(a, b)
        stdout.write("%s\n" % str(ret))

# call the main method
if __name__ == "__main__":
    #main()
    test()