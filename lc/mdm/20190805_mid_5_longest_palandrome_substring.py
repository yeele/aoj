#-*- coding: utf-8 -*-
from typing import List
import math


class Solution_n3:
    def longestPalindrome(self, s: str) -> str:
        #logging.basicConfig(level=logging.INFO, format="%(message)s")
        dp = [[-1]*len(s) for i in range(len(s))]
        # logging.debug("=== dp ===")
        # for row in dp:
        #     logging.debug(row)
        # logging.debug("=== main ===")
        for i in range(len(s)):
            for r in range(len(s)):
                for c in range(r, len(s)):
                    try:
                        x = dp[r][c+i]
                        if i == 0: dp[r][c+i] = 1
                        else: dp[r][c+i] = 0
                    except:
                        pass
                    break

        # logging.debug("=== dp ===")
        # for row in dp:
        #     logging.debug(row)
        if len(s) == 0: return s
        lp = s[0]
        # loop diagonally
        for i in range(len(s)):
            for r in range(len(s)):
                for c in range(r, len(s)):
                    try:
                        x = dp[r][c+i]
                        #logging.debug("(r, c+i) = (%d, %d)" % (r, c+i))
                        # 1-left-lower
                        try:
                            mid = dp[r+1][c+i-1]
                        except:
                            mid = 0
                        if s[r] == s[c+i] and (mid == 1 or mid == -1):
                            #logging.debug("--- hit ---")
                            dp[r][c+i] = 1
                            # update max
                            if c+i+1 - r > len(lp):
                                lp = s[r:c+i+1]
                        #logging.debug("mid[%s][%s](letters in the middle) is palandrome:%s" % (r+1, c+i-1, mid))

                    except:
                        pass
                    break

        # logging.debug("=== dp ===")
        # for row in dp:
        #     logging.debug(row)
        return lp


import time
def timeit(func):
    def wrapped(*args, **kwargs):
        start = time.time()
        ret = func(*args, **kwargs)
        elapsed = time.time() - start
        print("elapsed: %s" % elapsed)
        return ret
    return wrapped

class Solution_dp:
    @timeit
    def longestPalindrome(self, S: str) -> str:
        length = len(S)
        dp = [[0]*length for _ in range(length)]
        result = ""

        for offset in range(length):
            r = 0
            c = 0 + offset
            while r < length and c < length:
                if (r+1 < length and c-1 >= 0 and dp[r+1][c-1] == 1) or (c-1 < r+1):
                    if S[r] == S[c]: # This is palindrome
                        dp[r][c] = 1
                        if c+1 - r > len(result):
                            result = S[r:c+1]
                r+=1
                c+=1
        return result


"""
dp使わずに拡大していく方法
"""
class Solution:
    def expand_palindrome(self, S, i):
        l = i - 1
        r = i + 1
        result = S[i]
        while l >= 0 and r < len(S) and S[l] == S[r]: # check l and r within valid range
            # this is palindrome
            if r+1-l > len(result):
                result = S[l:r+1]
            l -= 1
            r += 1
        return result

    def expand_palindrome_2(self, S, i, j):
        l = i - 1
        r = j + 1
        if i < 0 or j >= len(S): return ""
        if S[i] != S[j]: return ""
        result = S[i:j+1]
        while l >= 0 and r < len(S) and S[l] == S[r]: # check l and r within valid range
            # this is palindrome
            if r+1-l > len(result):
                result = S[l:r+1]
            l -= 1
            r += 1
        return result

    @timeit
    def longestPalindrome(self, S: str) -> str:
        if len(S) <= 1: return S
        result = S[0]
        # palindrome starting with 1 char
        for i, c in enumerate(S):
            tmp = self.expand_palindrome(S, i)
            if len(tmp) > len(result):
                result = tmp
        # palindrome starting with 1 char
        for i, c in enumerate(S):
            tmp = self.expand_palindrome_2(S, i, i+1)
            if len(tmp) > len(result):
                result = tmp
        return result



import logging
logging.basicConfig(level=logging.INFO, format="%(message)s")
#logging.basicConfig(level=logging.DEBUG, format="%(message)s")
inputs = [
    "babad",
    "cbbd",
    # time-exceeded
    "kyyrjtdplseovzwjkykrjwhxquwxsfsorjiumvxjhjmgeueafubtonhlerrgsgohfosqssmizcuqryqomsipovhhodpfyudtusjhonlqabhxfahfcjqxyckycstcqwxvicwkjeuboerkmjshfgiglceycmycadpnvoeaurqatesivajoqdilynbcihnidbizwkuaoegmytopzdmvvoewvhebqzskseeubnretjgnmyjwwgcooytfojeuzcuyhsznbcaiqpwcyusyyywqmmvqzvvceylnuwcbxybhqpvjumzomnabrjgcfaabqmiotlfojnyuolostmtacbwmwlqdfkbfikusuqtupdwdrjwqmuudbcvtpieiwteqbeyfyqejglmxofdjksqmzeugwvuniaxdrunyunnqpbnfbgqemvamaxuhjbyzqmhalrprhnindrkbopwbwsjeqrmyqipnqvjqzpjalqyfvaavyhytetllzupxjwozdfpmjhjlrnitnjgapzrakcqahaqetwllaaiadalmxgvpawqpgecojxfvcgxsbrldktufdrogkogbltcezflyctklpqrjymqzyzmtlssnavzcquytcskcnjzzrytsvawkavzboncxlhqfiofuohehaygxidxsofhmhzygklliovnwqbwwiiyarxtoihvjkdrzqsnmhdtdlpckuayhtfyirnhkrhbrwkdymjrjklonyggqnxhfvtkqxoicakzsxmgczpwhpkzcntkcwhkdkxvfnjbvjjoumczjyvdgkfukfuldolqnauvoyhoheoqvpwoisniv",
    #"0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
]
for s in inputs:
    ans = Solution().longestPalindrome(s)
    logging.info(ans)