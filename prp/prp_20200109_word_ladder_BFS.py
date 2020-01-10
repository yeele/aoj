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
        stack = [source]
        mini = sys.maxsize
        dep = 0
        while len(stack) > 0:
            dep += 1
            if dep > len(words): return -1
            local_stack = []
            while len(stack) > 0:
                word = stack.pop()
                print("checking %s to %s" % (word, target))
                if word == target:
                    mini = min(mini, dep)
                    return mini
                for link in links[word]:
                    for next_word in lookup[link]:
                        if next_word != word:
                            if next_word not in local_stack:
                                local_stack.append(next_word)
                print("local_stack:%s" % local_stack)
            stack = local_stack
        return 0 if ans == sys.maxsize else ans + 1

ans = Solution().ladderLength(
"hit",
"cog",
["hot","dot","dog","lot","log","cog"]
)
print(ans)