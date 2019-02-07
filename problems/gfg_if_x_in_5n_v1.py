#-*- coding: utf-8 -*-
#https://www.geeksforgeeks.org/google-interview-experience/

from sys import stdin, stdout
def sol(x):
    print("sol(%s)" % x)
    if x % 5 == 0 and int(x/5) == 5: return True
    elif x % 5 == 0: return sol(int(x/5))
    return False




def test():
    x = 125
    x = 75
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


