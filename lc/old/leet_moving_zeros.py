#-*- coding: utf-8 -*-
class Solution_naive:
    def sol(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # nums are integer?
        # what to return if nums = None, or emply => return as it is
        """
        [0,1,0,3,12]
         i
         j
        """
        i = zeros = 0
        while i < len(nums): # i:1, nums:[1, 3, 12, 0, 0]
            if i >= len(nums)-zeros: break
            if nums[i] == 0: # nums[3]:0
                for j in range(i+1, len(nums)): # range(2, 5) => 2, 3, 4
                    nums[j-1] = nums[j]  # nums[1] = nums[2]
                nums[len(nums)-1] = 0 # [1, 3, 12, 0, 0]
                zeros+=1 # zeros:2
            else:
                i+=1 # 3
                print(i, nums)

class Solution:
    def sol(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # nums are integer?
        # what to return if nums = None, or emply => return as it is
        """
        [1,0,0,3,12]
         i
         j
         
        [0,1,0,3,12]
         i j
        最初が０なので０ポインターを0に、
        次に、ノンゼロポインターを１にセットして、スワップ。
        [1,0,0,3,12]
           i   j
        次に、最左のゼロポイを探す、index:1である、
        そして、最左のノンゼロポイを探す、index:3で値は３である、スワップ
        [1,3,0,0,12]
        次に、最左のゼロポイを探す、index:2である、
        そして、最左のノンゼロポイを探す、index:4で値は12である、スワップ
        [1,3,12,0,0]
                i    j
        """
        i = 0 # Zero pointer
        j = 0 # Non-Zero pointer
        # [1,3, 12,0,0]
        while i < len(nums) and j < len(nums): # # i:3, j:5
            # find zero pointer
            while i < len(nums) and nums[i] != 0:
                i+=1  # i:3
            print("i:%s, j:%s, nums:%s, len(nums):%s, nums[j]:%s" % (i, j, nums, len(nums), nums[j]))
            print("(nums[j] == 0):%s" % (nums[j] == 0))
            while (j < len(nums) and nums[j] == 0) or (j <= i):
                j+=1 # j:5
            if i < len(nums) and j < len(nums): # i:3, j:4
                tmp = nums[i]
                nums[i] = nums[j]
                nums[j] = tmp




nums = [0, 1, 0, 3, 12]
#nums = [0, 0, 1]
Solution().sol(nums)
print(nums)


