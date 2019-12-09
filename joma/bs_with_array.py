class Solution:
    def binary_search(self, S, k):
        if S is None or len(S) == 0: return -1
        if k is None: return -1
        sz = len(S)
        l = 0
        r = sz - 1
        while l <= r:
            m = (l + r) // 2
            print("l:%s <= r:%s" % (l, r))
            #真ん中より小さいかおおきいか？
            if S[m] == k:
                return m # indexを返したいので
            elif S[m] < k:
                l = m + 1
            else: # S[m] < k
                r = m - 1
        return -1



samples = [
    ([0, 1, 1, 2, 3, 4, 9 ], 4, 5),
    ([0, 1, 1, 2, 3, 4, 9 ], 7, -1),
    ([0, 1, 1, 2, 3, 4, 9 ], 0, 0),
    ([0, 1, 1, 2, 3, 4, 9 ], 1, 1),
]

for S, k, expected in samples:
    ans = Solution().binary_search(S, k)
    print(ans)
