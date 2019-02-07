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

def update_ans(S, i, j, ans):
    if ans is None: return S[i:j+1]
    elif len(S[i:j+1]) < len(ans):
        logging.debug("update_ans => miso11: overwriting ans:%s by %s" % (ans, S[i:j+1]))
        return S[i:j+1]
    return ans

def validate(S, i, j, arr):
    return all(x in S[i:j+1] for x in arr)

def increment(doExpand, i, j, S):
    def __increment(cur, last_index):
        if cur + 1 > last_index: return cur
        else: return cur+1
    if j == len(S)-1: # if already end
        i = __increment(i, len(S)-1)
    elif i >= j:
        j = __increment(j, len(S)-1)
    else:
        if doExpand: j = __increment(j, len(S)-1)
        else: i = __increment(i, len(S)-1)
    return (i, j)

def toggle(bool_a: bool):
    return not bool_a

def get_shortest_unique_substring(arr, S):
    ans = None
    i = j = 0
    do_expand = True
    while True:
        pre_do_expand = do_expand
        logging.info("while i:%s, j:%s validating %s do_expand:%s" % (i, j, S[i:j+1], do_expand))
        if validate(S, i, j, arr):
            ans = update_ans(S, i, j, ans)
            if pre_do_expand:
                do_expand = toggle(do_expand)
        else:
            if not pre_do_expand:
                do_expand = toggle(do_expand)
        (i, j) = increment(do_expand, i, j, S)
        logging.debug("nexti %s, j:%s" % (i, j))

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
#logging.basicConfig(level=logging.INFO, format="%(message)s")
logging.basicConfig(level=logging.WARN, format="%(message)s")
#print(get_shortest_unique_substring(['x', 'y', 'z'], "xyyzyzyx"))

#print(get_shortest_unique_substring(['a', 'b'], "abc"))
#print(get_shortest_unique_substring(['a', 'b'], "bzzzzaxyxybca")) # bca
#print(get_shortest_unique_substring(['a', 'b'], "bzzzzaxyxybc")) # bzzzza
#print(get_shortest_unique_substring(['a', 'b'], "bzzzzaxyxyabchhh")) # ab

#test
assert(get_shortest_unique_substring(['x', 'y', 'z'], "xyyzyzyx") == "zyx")
assert(get_shortest_unique_substring(['a', 'b'], "abc") == "ab")
assert(get_shortest_unique_substring(['a', 'b'], "bzzzzaxyxybca") == "bca") # bca
assert(get_shortest_unique_substring(['a', 'b'], "bzzzzaxyxybc") == "bzzzza") # bzzzza
assert(get_shortest_unique_substring(['a', 'b'], "bzzzzaxyxyabchhh") == "ab") # ab



