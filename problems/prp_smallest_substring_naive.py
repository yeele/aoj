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
def get_shortest_unique_substring(arr, str):
    for i in range(len(str)):
        tmp_ans = ""
        tmp = set()
        f_idx = None
        for j, c in enumerate(str[i:]):
            if c in arr:
                tmp.add(c)
                #print(c)
                if len(tmp) == 0:
                    if f_idx is None:
                        #print("m2. j:%s, c:%s" % (j, c))
                        f_idx = j
                if len(tmp) == len(arr): # completed
                    #print("m")
                    #print(f_idx, j)
                    tmp_ans = str[f_idx:j+1]
                    #print(tmp_ans)
                    tmp = set()
                    f_idx = None
        return tmp_ans


print(get_shortest_unique_substring(['a', 'b'], "abc"))
print(get_shortest_unique_substring(['a', 'b'], "bzzzzaxyxybca"))




"""
bzzzbaxyxybca
|     |
"""