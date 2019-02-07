#-*- coding: utf-8 -*-
"""
  arr = ['x', 'y', 'z']
  xyz
  xzy
  yxz
  yzx
  zxy
  zyx

  str.find(cmb)
  return cmb

  xyyzayzayx
  return "zayx"
  return "xyyz"


  arr = ab
  str = abc
  str = azbc  => azb
  str = bzac  => bza

  arr = [a,b]
  str = "bzzzzaxyxybca"
  b in arr -> yes
  z in arr -> no
  ...
  a in arr -> yes, if completed -> yes -> tmp_ans
  a in arr -> yes, if compelted -> yes(bca) -> update tmp_ans

  str = apple
  ""

  str = appleappleb
  tmp_ans = ""
  a in arr -> yes ,if completed -> no
  p, p, l, e,
  a in arr -> yes, if completed -> no
  p, p, l, e
  b in arry -> yes, if completed -> yes -> update tmp_ans

  str = appleapplebeeea
  tmp_ans = "appleappleb"
  beeea

  # O(N**2)
  # solution start from the where I found the last substring.(inclusive)

  str = appleapplebeeea
  str = appleapazabeeea
  """
def show_pointer(S, i, j):
    print("----------------")
    for m in range(len(S)+1):
        if m == i: print("i", end="")
        else: print(" ", end="")
    print("\n", end="")
    for m in range(len(S)+1):
        if m == i: print(m, end="")
        else: print(" ", end="")
    print("\n", end="")
    for s in S:
        print(s, end="")
    print("\n", end="")
    for m in range(len(S)+1):
        if m == j: print(m, end="")
        else: print(" ", end="")
    print("\n", end="")
    for m in range(len(S)+1):
        if m == j: print("j", end="")
        else: print(" ", end="")
    print("\n----------------")


def update_ans(S, arr, matched, i, j, ans):
    if len(matched) == len(arr) and len(S[i:j+1]) < len(ans):
        print("update_ans => miso11. matched: %s overwriting ans:%s by %s" % (matched, ans, S[i:j+1]))
        ans = S[i:j+1]
    return ans

def get_shortest_unique_substring(arr, S):
    i = j = 0
    matched = set()
    ans = S
    while i < len(S):
        print("miso1 S[i:j+1]:%s, i:%s, j:%s" % (S[i:j+1], i, j))
        while j < len(S) and S[j] in arr:
            show_pointer(S, i, j)
            print("J query => miso2 adding element S[j] onto matches S[j]:%s i:%s, j:%s, matched:%s" % (S[j], i, j, matched))
            matched.add(S[j])
            print("J query => miso3 added  element S[j] onto matches S[j]:%s i:%s, j:%s, matched:%s" % (S[j], i, j, matched))
            if len(matched) == len(arr):
                print("J query => miso4 breaking J query loop")
                ans = update_ans(S, arr, matched, i, j, ans)
                break
            print("J query => miso5 incrementing j++")
            j+=1
        watch = S[i]
        while i < len(S):
            show_pointer(S, i, j)
            print("I query => miso10 i:%s, j:%s, matched:%s, S[i:j+1]:%s" % (i, j, matched, S[i:j+1]))
            if S[i] != watch:
                print("I query => miso12. removing watch:%s from matched:%s" % (watch, matched))
                matched.remove(watch)
                print("I query => miso13. removed watch:%s from matched:%s" % (watch, matched))
                print("I query => miso14. breaking I query loop")
                break
            else:
                ans = update_ans(S, arr, matched, i, j, ans)
            print("I query => miso15. incrementing i++")
            i+=1

        if j < len(S)-1:
            print("J query => miso5 incrementing j++")
            j+=1


    return ans

"""
解けてません
iをヅラしていく、S[i] != watchでは、うまくmatched を削除できませんyyzyyxの時に
yyzの時にyを削除してしまうが、これでは中央(zyyx)のyを削除してしまい、
意図していない
"""
print(get_shortest_unique_substring(['x', 'y', 'z'], "xyyzyzyx"))
# print(get_shortest_unique_substring(['a', 'b'], "abc"))
# print(get_shortest_unique_substring(['a', 'b'], "bzzzzaxyxybca"))




