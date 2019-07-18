#-*- coding: utf-8 -*-
from typing import List
class Solution:
    def sol_for_2(self, target_sum, chosen, S):
        # -1, [-1], [-1, 0, 1, -1, 4, 2]
        cache = {}
        anss = set()
        """
        -1: 0 # -1 - (-1) = 0
        0: 
          --> chosen[-1] + [-1, 0]
        0: 1  # 0 - (-1) = 1
        1
        --> chosen[-1] + [0, 1]
        1: -1
        """
        for s in S: # [-1, 0, 1, -1, 4, 2]
            if s in cache.values():
                ans = chosen + [s, cache[s]]
                anss.append(ans)
            cache[s] = s - target_sum
        return anss


    def rec(self, target_sum, num_elements, S, chosen=[]):
        if num_elements == 2:
            return self.sol_for_2(target_sum, chosen, S)
        elif num_elements > 2:
            answers = []
            for s in S:
                copied = S[:]
                copied.remove(s)
                chosen_copied = chosen[:]
                chosen_copied.append(s)
                ans = self.rec(target_sum + s, num_elements - 1, S, chosen_copied)
                answers.append(ans)
        else:
            return []


    def sol(self, S):
        self.rec(0, 3, S)

    def bruteforce(self, S):
        for i in range(len(S)):
            for j in range(len(S)):
                for k in range(len(S)):
                    if i != j and j != k:
                        if S[i] + S[j] + S[k] == 0:
                            print(S[i], S[j], S[k])


    def blackbox(self, a, b, c):
        return a + b + c

    def joma(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        print("nums:%s" % nums)
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            j = i + 1
            k = len(nums)-1
            print("i:%s, j:%s, k:%s" % (i, j, k))
            while j < k:
                I = nums[i]
                J = nums[j]
                K = nums[k]
                print("I:%s, J:%s, K:%s" % (I, J, K))
                T = self.blackbox(I, J, K)
                if T == 0:
                    res.append([I, J, K])
                    j+=1;
                    while nums[j] == nums[j-1]: j+=1
                elif T > 0:
                    k-=1;
                    while nums[k] == nums[k+1]: k-=1
                else: # T <0
                    j+=1;
                    while nums[j] == nums[j-1]: j+=1

        return res



S = [-1, 0, 1, -1, 4, 2]
#print(Solution().sol(S))
#print(Solution().bruteforce(S))
print(Solution().joma(S))



