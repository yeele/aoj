#-*- coding: utf-8 -*-
"""
https://techdevguide.withgoogle.com/paths/foundational/sequence-2/find-longest-word-in-dictionary-that-subsequence-of-given-string/#code-challenge


"""


def lcs(S, W):
    dp = [[0] * (len(S)+1) for _ in range(len(W)+1)]
    for i, w in enumerate(W):
        i+=1
        for j, s in enumerate(S):
            j+=1
            if s == w:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    # for row in dp:
    #     print (row)
    return dp[-1][-1]
def sol_mine(S, D):
    maxi = 0
    ans = None
    for W in D:
        sz = lcs(S, W)
        if sz > 0: print(S, W, sz)
        if sz > maxi:
            maxi = sz
            ans = W
    return ans


import collections
import sys
def find_longest_word_in_string(letters, words):
    letter_positions = collections.defaultdict(list)
    # For each letter in 'letters', collect all the indices at which it appears.
    # O(#letters) space and speed.
    for index, letter in enumerate(letters):
        letter_positions[letter].append(index)
    print(letter_positions)
    # For words, in descending order by length...
    # Bails out early on first matched word, and within word on
    # impossible letter/position combinations, but worst case is
    # O(#words # avg-len) * O(#letters / 26) time; constant space.
    # With some work, could be O(#W * avg-len) * log2(#letters/26)
    # But since binary search has more overhead
    # than simple iteration, log2(#letters) is about as
    # expensive as simple iterations as long as
    # the length of the arrays for each letter is
    # “small”.  If letters are randomly present in the
    # search string, the log2 is about equal in speed to simple traversal
    # up to lengths of a few hundred characters.
    for word in sorted(words, key=lambda w: len(w), reverse=True):
        pos = 0
        for letter in word:
            if letter not in letter_positions:
                break
            # Find any remaining valid positions in search string where this
            # letter appears.  It would be better to do this with binary search,
            # but this is very Python-ic.
            possible_positions = [p for p in letter_positions[letter] if p >= pos]
            if not possible_positions:
                break
            pos = possible_positions[0] + 1
            # We didn't break out of the loop, so all letters have valid positions
            return word



def sol(S, D):
    return find_longest_word_in_string(S, D)


# import sys
# sys.setrecursionlimit(314159265)
test = False
test = True
if test:
    # n, k = 5, 5
    #S =list( map(int, "4 2 6".split()))

    # S = "abppplee"
    # W = "apple"
    # print(sol(S, W))
    #
    # S = "heat"
    # W = "hit"
    # print(sol(S, W))
    #
    S = "abppplee"
    W = "kangaroo"
    print(lcs(S, W))
    #print(lcs_v1(S, W))


    S = "abppplee"
    D = ["able", "ale", "apple", "bale", "kangaroo"]
    print(sol(S, D))


else:
    #n, k = map(int, input().split())
    S =list( map(int, input().split()))
    k, a, b = S
    print(sol(k, a, b))


