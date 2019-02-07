#-*- coding: utf-8 -*-
"""
https://www.pramp.com/challenge/8noLWxLP6JUZJ2bA2rnx
コメントで声に出しながら
一行術デバッグしていくのは秀逸やった。パクろう

"""
def encrypt(word):
    ans = ""
    pre = 1
    for c in word:
        pre = ord(c) + pre # 99 + 1
        tmp = pre
        while tmp > ord('z'):
            tmp -= 26
        ans += chr(tmp)
    return ans

def decrypt(word):
    ans = ""
    pre = 1 # 100
    pre2 = 0
    for c in word: # 110
        tmp = ord(c) - pre # 110 - 100 = 10
        while tmp < ord('a'):
            tmp += 26 # 10, 36, 62, 88, 114
        pre = pre + tmp
        print(pre, ord(c), pre-ord(c), (pre-ord(c))%26)
        ans += chr(tmp)
    return ans

"""
  c   r   i   m   e
 99 114	105	109	101
  1 100 214 319 428
100 214 319 428 529
100	110	111	116	113
  d   n	  o	  t	  q
  
  
  d   n	  o	  t	  q
100	110	111	116	113
  1 100 110 111 116
 99  10   1   5  -3
 99 114 105 109 101
"""



print(encrypt("crime"))
print(decrypt("dnotq"))

