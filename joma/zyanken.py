#-*- coding: utf-8 -*-
"""
"""


import random



HANDS = {
    0: 'ぐー',
    1: 'ちょき',
    2: 'ぱー',
}


while True:
    input("じゃん・けん・")
    print("ぽん！！")
    hand = random.randint(0, 2)
    print(HANDS[hand])

