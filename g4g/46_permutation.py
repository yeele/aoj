from typing import List
class Solution_ok:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def rec(options, chosen):
            ans = []
            nums = options[:]
            #print(options, chosen)
            if len(options) == 0:
                #print(chosen)
                ans.append(chosen)
            else:
                for i in range(len(nums)):
                    options = nums[:]
                    chosen_copy = chosen[:]
                    chosen_copy.append(nums[i])
                    del options[i]
                    ans += rec(options, chosen_copy)
            return ans
        return rec(nums, [])

# okより少しだけ無駄を省いた。
class Solution_ok2:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def rec(options, chosen):
            ans = []
            if len(options) == 0:
                ans.append(chosen)
            else:
                for i in range(len(options)):
                    options_copy = options[:]
                    chosen_copy = chosen[:]
                    chosen_copy.append(options[i])
                    del options_copy[i]
                    ans += rec(options_copy, chosen_copy)
            return ans
        return rec(nums, [])


class Solution_backtrack:
    """
    1 2 3
    [1] .. [1 3] .. [ 1 3 2 ]
    """
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(nums, chosen, permutations):
            if len(chosen) == len(nums):
                # chosen[:]のコピーであることに注意！バックトラックではchosenを使いまわしているので、
                # こうする必要があることに注意。
                permutations.append(chosen[:])
            else:
                for i in range(len(nums)):
                    # 入力の特徴を活かす
                    # collection of distinct integers, return all possible permutations.
                    if nums[i] not in chosen:
                        chosen.append(nums[i])
                        backtrack(nums, chosen, permutations)
                        chosen.remove(nums[i])

        permutation, permutations = [], []
        backtrack(nums, permutation, permutations)
        return permutations


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def rec(options, chosen):
            ans = []
            if len(options) == 0:
                ans.append(chosen[:])
            else:
                N = len(options)
                for i in range(N):
                    value = options[i]
                    chosen.append(value)
                    options.remove(value)
                    ans += rec(options, chosen)
                    # 元に戻す
                    options.insert(i, value) # どこに戻すか？が重要で、以前と同じ場所でないと、いけない.
                    chosen.remove(value)
            return ans

        return rec(nums[:], [])

"""
1 2 3
1 3 2
2 1 3
2 3 1
3 1 2 
3 2 1
"""
ans = Solution().permute([1, 2, 3])
print(ans)