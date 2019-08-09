#-*- coding: utf-8 -*-
class Solution:
    def sortedSquares(self, S):
        if len(S) == 0: return S
        # i is current pointer, j is pointer to help going back
        # # [-4, -1, 0, 3, 10]
        S[0] = abs(S[0])**2 # # [16, -1, 0, 3, 10]
        i = j = 1
        while i < len(S): # [0, 1, 9, 16, 10], i:4
            j = i # i:4, j:4
            S[i] = abs(S[i])**2 # [0, 1, 9, 16, 100]
            while j > 0 and S[j-1] > S[i]: # 16 < 100
                j-=1 # j:2
            if j < i: # swap # i:3,j:2, S:[0, 1, 16, 9, 10]
                tmp = S.pop(i) # [0, 1, 16, 10]
                S.insert(j, tmp) # # [0, 1, 9, 16, 10]
            i+=1 # i:5
        return S


S = [-4, -1, 0, 3, 10]
S = list(range(1000, 500, -1))+list(range(0, 1000, 1))
#print(S)
print(Solution().sortedSquares(S))



