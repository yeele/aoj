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

def update_ans(S, i, j, ans):
    if ans is None: return S[i:j+1]
    elif len(S[i:j+1]) < len(ans):
        logging.debug("update_ans => miso11: overwriting ans:%s by %s" % (ans, S[i:j+1]))
        return S[i:j+1]
    return ans

def validate(S, i, j, arr):
    return all(x in S[i:j+1] for x in arr)

def validate2(dup, arr):
    return len(dup) == len(arr)

def increment(doExpand, i, j, S):
    def __increment(cur, last_index):
        if cur + 1 > last_index: return cur
        else: return cur+1
    if j == len(S)-1: # if already end
        i = __increment(i, len(S)-1)
        next = 'i'
    elif i >= j:
        j = __increment(j, len(S)-1)
        next = 'j'
    else:
        if doExpand:
            j = __increment(j, len(S)-1)
            next = 'j'
        else:
            i = __increment(i, len(S)-1)
            next = 'i'
    return (i, j, next)

def toggle(bool_a: bool):
    return not bool_a

def update_dup(dup, added, deled, arr, S, i, j):
    logging.debug("dup before: %s" % dup)
    if added and added in arr:
        dup.add(added)
    if deled and deled in dup and not deled in S[i:j+1]:
        dup.remove(deled)
    logging.debug("dup after: %s" % dup)


def get_shortest_unique_substring(arr, S):
    ans = None
    if len(S) == 0: return None
    i = j = 0
    do_expand = True
    dup = set()
    added = S[0]
    deled = None
    while True:
        logging.info("while i:%s, j:%s validating %s do_expand:%s, added:%s deled:%s" % (i, j, S[i:j+1], do_expand, added, deled))
        update_dup(dup, added, deled, arr, S, i, j)
        if validate2(dup, arr):
            logging.info("validated")
            ans = update_ans(S, i, j, ans)
            if do_expand:
                do_expand = toggle(do_expand)
        else:
            logging.info("Not-validated")
            if not do_expand:
                do_expand = toggle(do_expand)
        (pre_i, pre_j) = (i, j)
        (i, j, next) = increment(do_expand, i, j, S)
        logging.debug("i:%s j:%s next:%s, pre_i:%s pre_j:%s" % (i, j, next, pre_i, pre_j))
        if 'j' == next:
            added = S[j]
            deled = None
        elif 'i' == next:
            added = None
            deled = S[pre_i]
        logging.debug("next i %s, j:%s, added:%s deled:%s" % (i, j, added, deled))
        #show_pointer(S, i, j)
        if j == len(S)-1 and i == len(S)-1:
            break

    return ans

"""
解けてません
iをヅラしていく、S[i] != watchでは、うまくmatched を削除できませんyyzyyxの時に
yyzの時にyを削除してしまうが、これでは中央(zyyx)のyを削除してしまい、
意図していない
ということでv4を作成しています、
ここではiをずらし行き、毎回S[i:j+1]が条件を致しているかを
確認することとします
あかん、なんとなく全然v4までうまく動いてないやん。
ちょっと、一回リセットして解き直す。それがv5

やっと全てのテストケースが通りました。okバージョンです。
v6では、validate がO(n) なので、結局O(n**2)担っているのを改善します
"""
import logging
#logging.basicConfig(level=logging.DEBUG, format="%(message)s")
#logging.basicConfig(level=logging.INFO, format="%(message)s")
#logging.basicConfig(level=logging.WARN, format="%(message)s")
#print(get_shortest_unique_substring(['x', 'y', 'z'], "xyyzyzyx"))

#print(get_shortest_unique_substring(['a', 'b'], "abc"))
# print(get_shortest_unique_substring(['a', 'b'], "bzzzzaxyxybca")) # bca
# print(get_shortest_unique_substring(['a', 'b'], "bzzzzaxyxybc")) # bzzzza
#print(get_shortest_unique_substring(['a', 'b'], "bzzzzaxyxyabchhh")) # ab

#test
assert(get_shortest_unique_substring(['x', 'y', 'z'], "xyyzyzyx") == "zyx")
assert(get_shortest_unique_substring(['a', 'b'], "abc") == "ab")
assert(get_shortest_unique_substring(['a', 'b'], "bzzzzaxyxybca") == "bca") # bca
assert(get_shortest_unique_substring(['a', 'b'], "bzzzzaxyxybc") == "bzzzza") # bzzzza
assert(get_shortest_unique_substring(['a', 'b'], "bzzzzaxyxyabchhh") == "ab") # ab



