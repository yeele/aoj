#-*- coding: utf-8 -*-
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import defaultdict
        cache = defaultdict(int)
        for i in nums:
            cache[i] += 1

        a = [(key, value) for key, value in cache.items()]
        #print ("a:%s" % a)
        b = sorted(a, key = lambda value: value[1], reverse=True)
        #print ("b:%s" % b)
        return [ b[j][0] for j in range(k)]