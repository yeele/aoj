from typing import List
from collections import defaultdict
import sys
def rep(s, index, newstring):
    return s[:index] + newstring + s[index + 1:]

class Solution:
    def ladderLength(self, source: str, target: str, words: List[str]) -> int:

        lookup = defaultdict(list)
        links  = defaultdict(list)
        for word in words + [source]:
            for i in range(len(word)):
                link = rep(word, i, '-')
                lookup[link].append(word)
                links[word].append(link)
                #print(lookup)
        # print(lookup)
        # print(links)
        cache = {} # defaultdict(int)
        def rec(word, target, seen, dep):
            if word in cache:
                return cache[word]
            #print(word, target)
            if word == target:
                if word in cache: cache[word] = min(dep, cache[word])
                else: cache[word] = dep
                return dep
            else:
                seen.append(word)
                local = sys.maxsize
                for link in links[word]: # -it, b-t, -it
                    for next_word in lookup[link]: # list of words,
                        if next_word == word: continue
                        if not next_word in seen:
                            mini_dep = rec(next_word, target, seen, dep+1)
                            #cache[next_word] = mini_dep
                            local = min(local, mini_dep)
                seen.remove(word)
                #cache[word] = local
                return local

        seen = []
        ans = rec(source, target, seen, 0)
        print(cache)
        return 0 if ans == sys.maxsize else ans + 1

ans = Solution().ladderLength(
"hit",
"cog",
["hot","dot","dog","lot","log","cog"]
)
print(ans)