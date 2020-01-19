#https://leetcode.com/problems/word-ladder/discuss/473774/python-two-end-solution-100ms
from typing import List
from collections import defaultdict
import sys
def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
    # https://leetcode.com/problems/word-ladder/discuss/461462/Python-BFS-List-Comprehension
    import collections
    dict = set(wordList)
    if endWord not in dict: return 0

    q = collections.deque([beginWord])
    step = 0
    while q:
        size = len(q)
        for s in range(size):
            top = q.popleft()
            next_words = [top[:i] + ch + top[i+1:] for i in range(len(top)) for ch in string.ascii_lowercase]
            for next in next_words:
                if next == endWord: return step + 2
                if next not in dict: continue
                dict.remove(next)
                q.append(next)
        step += 1
    return 0

#https://leetcode.com/problems/word-ladder/discuss/473774/python-two-end-solution-100ms
class Solution_lc:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        counts = 1
        letters = 'abcdefghijklmnopqrstuvwxyz'
        if beginWord in wordList:
            wordList.remove(beginWord)
        word_dic = {i:1 for i in wordList} # for O(1) search
        l = set([beginWord])
        r = set([endWord])
        ll = set([beginWord]) # record all the words appeared
        #rr = set([endWord])

        while l:
            tmp = []
            for word in l:
                for ch in letters:
                    for i in range(len(word)):
                        new = word[:i]+ch+word[i+1:]
                        if (new not in ll) & (new in word_dic):
                            tmp.append(new)
            l = set(tmp)
            counts += 1
            ll = ll | l

            if l & r:
                return counts
            # これを入れたら動かんかったし、読んでいてもおかしいコード。だから外す。
            # if len(l) > len(r):
            #     l, r, ll, rr = r, l, rr, ll # for less branches


        return 0

def timeit(func):
    def wrapped(*args, **kwargs):
        start = time.time()
        ret = func(*args, **kwargs)
        elapsed = time.time() - start
        print("elapsed: %s" % elapsed)
        return ret
    return wrapped

from collections import defaultdict
import time

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        if rooms is None: return False
        if len(rooms) <= 1: return True
        visited = [0] * len(rooms)
        stack = [0]
        counter = 0
        # rooms = [[3], [], [3], [0, 2]]
        while stack: # [0]
            room_idx = stack.pop()  # room_idx = 0
            if visited[room_idx] == 1:
                # 既に訪問
                pass
            else:
                for key in rooms[room_idx]:
                    stack.append(key) # stack = []
                visited[room_idx] = 1 # [1, 0, 1, 1]
                counter += 1

        # O(N)
        #print(visited)
        #return all(visited)
        return counter == len(rooms)

S = [[1],[2],[3],[]]
ans = Solution().canVisitAllRooms(S)
print(ans)
