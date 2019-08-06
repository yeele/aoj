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

class Solution:
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




import logging
logging.basicConfig(level=logging.INFO, format="%(message)s")
#logging.basicConfig(level=logging.DEBUG, format="%(message)s")
s = "babad"
s = "cbbd"
# time-exceeded
#s = "kyyrjtdplseovzwjkykrjwhxquwxsfsorjiumvxjhjmgeueafubtonhlerrgsgohfosqssmizcuqryqomsipovhhodpfyudtusjhonlqabhxfahfcjqxyckycstcqwxvicwkjeuboerkmjshfgiglceycmycadpnvoeaurqatesivajoqdilynbcihnidbizwkuaoegmytopzdmvvoewvhebqzskseeubnretjgnmyjwwgcooytfojeuzcuyhsznbcaiqpwcyusyyywqmmvqzvvceylnuwcbxybhqpvjumzomnabrjgcfaabqmiotlfojnyuolostmtacbwmwlqdfkbfikusuqtupdwdrjwqmuudbcvtpieiwteqbeyfyqejglmxofdjksqmzeugwvuniaxdrunyunnqpbnfbgqemvamaxuhjbyzqmhalrprhnindrkbopwbwsjeqrmyqipnqvjqzpjalqyfvaavyhytetllzupxjwozdfpmjhjlrnitnjgapzrakcqahaqetwllaaiadalmxgvpawqpgecojxfvcgxsbrldktufdrogkogbltcezflyctklpqrjymqzyzmtlssnavzcquytcskcnjzzrytsvawkavzboncxlhqfiofuohehaygxidxsofhmhzygklliovnwqbwwiiyarxtoihvjkdrzqsnmhdtdlpckuayhtfyirnhkrhbrwkdymjrjklonyggqnxhfvtkqxoicakzsxmgczpwhpkzcntkcwhkdkxvfnjbvjjoumczjyvdgkfukfuldolqnauvoyhoheoqvpwoisniv"
s = "0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
ans = Solution().longestPalindrome(s)
logging.info(ans)