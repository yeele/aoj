#-*- coding: utf-8 -*-
"""
https://www.pramp.com/challenge/8noLWxLP6JUZJ2bA2rnx
"""
def encrypt(word):
    encrypted = ""
    for i, w in enumerate(word):
        pre = 0 if i == 0 else step2
        step1 = ord(w)
        step2 = step1 + 1 if i == 0 else step1 + pre
        step3 = step2 - (((step2 - ord('z')) / 26) + 1) * 26
        encrypted += chr(step3)
    return encrypted


def decrypt(word):
    for i, e in enumerate(word):
        step3 = ord(e)
        print (step3)
    pass # your code goes here


e = encrypt("crime")
print( e)
print( decrypt(e) )

