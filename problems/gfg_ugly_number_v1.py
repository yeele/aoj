#code
#https://practice.geeksforgeeks.org/problems/ugly-numbers/0
from sys import stdin, stdout
from collections import defaultdict


def un(n):
    dp = defaultdict(int)
    dp[1] = 1
    cur_n = 1
    i = 2
    last = 0
    while cur_n < n:
        #print("%s...." % i)
        for p in [2, 3, 5]:
            if i % p == 0 and dp[int(i/p)] == 1:
                dp[i] = 1
                cur_n += 1
                break
            else:
                dp[i] = 0
        last = i
        i+=1

    print(dp)
    return last


def test():
    n = 10 #expected = 12
    #n = 4 #expected = 4
    ret = un(n)
    stdout.write("%s\n" % str(ret))

def main():
    n_ts = int(stdin.readline())
    for i in range(n_ts):
        n = int(stdin.readline().strip())
        ret = un(n)
        stdout.write("%s\n" % str(ret))

# call the main method
if __name__ == "__main__":
    #main()
    test()