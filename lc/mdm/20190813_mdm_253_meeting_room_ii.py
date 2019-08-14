#Definition for singly-linked list.
from typing import List

class Solution:
    def minMeetingRooms(self, S: List[List[int]]) -> int:
        if S is None or len(S) == 0: return 0
        S.sort(key=lambda se: se[0])
        max_room = 1
        cur_room = 1
        dup_room = 1
        dup_s = dup_e = None
        pre_s = pre_e = None
        for i, (s, e) in enumerate(S):
            if i == 0:
                pass
            else:
                if dup_e and s <= dup_e: # 連続かぶりとの比較パターン
                    dup_s = max(dup_s, s)
                    dup_e = min(dup_e, e)
                    dup_room += 1
                    max_room = max(max_room, dup_room)
                    cur_room = 1
                elif s <= pre_e: # 直前と比較パターン
                    dup_s = max(pre_s, s)
                    dup_e = min(pre_e, e)
                    cur_room += 1
                    max_room = max(max_room, cur_room)
                    dup_room = 1
                    dup_s = dup_e = None
                else:
                    cur_room = 1
            pre_s = s
            pre_e = e
        return max_room

samples = [
    [[0, 30], [2, 10],[15, 25] ],
    [[0, 30], [2, 20],[15, 25] ],
    [[0, 14], [15, 25] ],
    [[0, 15], [15, 25] ],
    # unsorted
    [[7, 10], [2, 4] ],
    [[12, 20], [7, 10], [0, 100] ],

]
for S in samples:
    ans = Solution().minMeetingRooms(S)
    print("%s = %d" % (S, ans))
