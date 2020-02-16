#https://leetcode.com/problems/word-ladder/discuss/473774/python-two-end-solution-100ms
from typing import List
from collections import defaultdict
import sys

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
    def ladderLength(self, S: str, T: str, words: List[str]) -> int:
        if S is None or T is None: return 0
        if len(S) != len(T): return 0
        if T not in words: return 0       # tO(N)

        # hit -> hot
        # hit -> a(it), b(it), c(it), ... z(it)
        # 3 * 26 --------> len(M) * 26

        """
        hit
        visited = 
        """
        lookup = { word:0 for word in words}
        lookup[S] = 0
        #print(lookup)
        import string
        from functools import lru_cache
        cache = {}
        def dfs(curr):
            #print(sS"dfs(%s)" % (curr))
            if curr not in lookup or lookup[curr] == 1: return []
            lookup[curr] = 1
            local = None
            for i in range(len(curr)):
                #print(curr[:i] + '*' + curr[i+1:])
                for r in string.ascii_lowercase:
                    tugi = curr[:i] + r + curr[i+1:]
                    if tugi == curr: continue
                    #print(tugi, end=',')
                    if tugi in lookup:
                        #print(tugi)
                        if tugi == T:
                            return [tugi]
                        ret = dfs(tugi)
                        if isinstance(ret, list) and len(ret) > 0:
                            tmp = [tugi] + ret
                            if local is None:
                                local = tmp
                            else:
                                if len(tmp) < len(local):
                                    local = tmp
            return [] if local is None else local

        ans = dfs(S)
        if len(ans) > 0:
            ans = [S] + ans
        #print(ans)
        return len(ans)


# SPEND HOURS...
# 最後にみたよ。。。できんかったから。
# https://leetcode.com/problems/word-ladder/discuss/494234/BFS-simple-BFS-and-2-end-BFS-in-Python



samples = [
    (
        "hit",
        "cog",
        ["hot","dot","dog","lot","log","cog"]
    ),
    (
        "hot",
        "dog",
        ["hot","dog","dot"]
    ),
    (
        "kiss",
        "tusk",
        ["miss","dusk","kiss","musk","tusk","diss","disk","sang","ties","muss"]
    ),
    (
        "qa",
        "sq",
        ["si","go","se","cm","so","ph","mt","db","mb","sb","kr","ln","tm","le","av","sm","ar","ci","ca","br","ti","ba","to","ra","fa","yo","ow","sn","ya","cr","po","fe","ho","ma","re","or","rn","au","ur","rh","sr","tc","lt","lo","as","fr","nb","yb","if","pb","ge","th","pm","rb","sh","co","ga","li","ha","hz","no","bi","di","hi","qa","pi","os","uh","wm","an","me","mo","na","la","st","er","sc","ne","mn","mi","am","ex","pt","io","be","fm","ta","tb","ni","mr","pa","he","lr","sq","ye"]
    )

]
for s, t, D in samples:
    ans = Solution().ladderLength(s, t, D)
    print(ans)
