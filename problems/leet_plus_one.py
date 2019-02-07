#-*- coding: utf-8 -*-
"""

S = [1, 2, 3]
len = 3
1st: 3-1-0 = 10**2 = 100
2nd: 3-1-1 = 10**1 =  10
2nd: 3-1-2 = 10**0 =   1

ttl = sum( x*10**( len(S)-1-i ) for i, x in S )

add 1.
carry = 0
if x >= 10
While 3 to 1
cur+1+carry
if cur >= 10:
  S[i] = cur % 10
  carry = int(cur/10)
  xx
else:
    break

if cur is None and carry, then S.put(0) # insert in index

O(N)
Space O(1)


#Recursive
rec(S, i)
if i == len(S)-1:
  S[i] = (S[i] + 1) % 10
  carry = int((S[i] + 1) / 10)
  return carry
else:
    S[i] = S[i] + rec(S, i+1)
    carry = int((S[i] + 1) / 10)
    return carry




"""

class Solution:
    def rec(self, S, i):
        if i == len(S)-1:
            print("rec:%i, S[i]:%s" % (i, S[i]))
            carry = int((S[i] + 1) / 10)
            S[i] = (S[i] + 1) % 10
            print("carry:%s" % carry)
            return carry
        else:
            pre_carry = self.rec(S, i+1)
            carry = int((S[i] + pre_carry) / 10)
            S[i] = (S[i] + pre_carry) % 10
            print("rec:%i, S[i]:%s" % (i, S[i]))
            print("carry:%s" % carry)
            return carry

    def sol(self, S):
        S = [0] + S
        rec = self.rec(S, 0)
        if S[0] == 0: S.pop(0)
        return S



import logging
logging.basicConfig(level=logging.INFO, format="%(message)s")
S = [1, 2, 3]
S = [1, 2, 9]
S = [1, 9, 9]
S = [9, 9, 9]

print(Solution().sol(S))


