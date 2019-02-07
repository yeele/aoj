#-*- coding: utf-8 -*-
#one of the guy said , this question was asked during the interview.
#https://www.geeksforgeeks.org/google-interview-experience-set-7-software-engineering-intern/

from sys import stdin, stdout

def sol2(x):
    import re
    return re.sub("\s+", " ", x)

def sol(x):
    pre = ""
    ans = ""
    for i, c in enumerate(x):
        if pre == " " and c == " ":
            continue
        else:
            #print(i, c, end="")
            ans += c
        pre = c
    return ans

def test():
    x = "I   love  on   earth"
    expected = "I love on earth"
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


