#-*- coding: utf-8 -*-
import time
def timeit(func):
    def wrapped(*args, **kwargs):
        start = time.time()
        ret = func(*args, **kwargs)
        elapsed = time.time() - start
        print("elapsed: %s" % elapsed)
        return ret
    return wrapped

class Solution:
    def __init__(self):
        self.cache = {}
        self.hit = 0
        self.ttl = 0

    def rec(self, chosen, remain):
        #print(chosen, remain)
        ans = []
        if remain <= 0:
            if remain == 0:
                return [chosen]
            else:
                return []
        else:
            ret1 = self.rec(chosen+",1", remain -1)
            #print("ret1:%s" % ret1)
            ret2 = self.rec(chosen+",2", remain -2)
            #print("ret2:%s" % ret2)
            ans.extend(ret1)
            ans.extend(ret2)
            return ans


    #再起でキャッシュなし　(30) => 1.8sec
    @timeit
    def sol(self, steps):
        return self.rec("", remain=steps)

    def rec_cache(self, chosen, remain):
        self.ttl += 1
        #print(chosen, remain)
        if (chosen, remain) in self.cache:
            self.hit +=1
            return self.cache[(chosen, remain)]
        ans = []
        if remain <= 0:
            if remain == 0:
                self.cache[(chosen, remain)] = 1
                return 1
            else:
                self.cache[(chosen, remain)] = 0
                return 0
        else:
            ret1 = self.rec_cache(chosen+",1", remain -1)
            self.cache[(chosen+",1", remain-1)] = ret1
            #print("ret1:%s" % ret1)
            ret2 = self.rec_cache(chosen+",2", remain -2)
            self.cache[(chosen+",2", remain-2)] = ret2
            #print("ret2:%s" % ret2)
            self.cache[(chosen, remain)] = ret1 + ret2
            return ret1 + ret2
    #再起でキャッシュあり
    @timeit
    def sol3(self, steps):
        ret = self.rec_cache("", steps)
        print("ttl:%s, hit:%s, hit-ratio:%s" % (self.ttl, self.hit, self.hit/self.ttl))
        print(self.cache.keys()[0:10])
        return ret


    @timeit
    def sol2(self, steps):
        dp = [0]*(steps+1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, steps+1):
            print(dp)
            print(i)
            dp[i] = dp[i-1] + dp[i-2]
        return dp[-1]




#print(Solution().sol2(30))

ret = Solution().sol3(30)
print(ret)

#ret = Solution().sol(30)
#for r in ret: print(r)
#print(len(ret))




