#-*- coding: utf-8 -*-
"""
"""
import logging
logging.basicConfig(level=logging.DEBUG, format="%(message)s")
import binascii


def sol(S):
    #print(S, len(S))
    return binascii.unhexlify(S)



hex_str = """
74686520616e7377657220796f75207365656b20696e207468652073756d206f6520796f7572206a
6f75726e657920746f2074686520686f72697a6f6e20616e6420746f207468652073746172732079
6f752077696c6c2066696e6420696e207468652072656d61696e73206f6620746865206c6f6e6765
7374207061746820616e6420746865206465787468206f6620746865206f6365616e
"""
print(sol(hex_str.replace('\n', '').replace('\r', '').strip()))


def g_encode(S, n = 1):
    # ans = ""
    # for s in S:
    #     tmp = ord(s) + 13
    #     if tmp > 122: tmp = (tmp % 122) + (60-1)
    #     ans += chr(tmp)
    # return ans
    return "".join([chr(ord(s) + 13) for s in S])

def g_decode(S, n=1):
    # ans = ""
    # for s in S:
    #     tmp = ord(s) - 13
    #     if tmp < 60: tmp = (122+1) - (tmp % 60)
    #     ans += chr(tmp)
    # return ans
    return "".join([chr(ord(s) - 13) for s in S])
    #return [encode_map[s.lower()] for s in S].join("")

def g_decode_n(S, n=13):
    # ans = ""
    # for s in S:
    #     tmp = ord(s) - 13
    #     if tmp < 60: tmp = (122+1) - (tmp % 60)
    #     ans += chr(tmp)
    # return ans
    return "".join([chr(ord(s) - n) for s in S])

str = """
00. I hope this transmission finds you well, and all is under control.
01. It's been too long. Then again, how do you measure the time?
02. I'm putting myself to good use here, but often miss the old domain.
03. Sometimes, upon the darkest night, I'm brought back to that morning light.
04. There's no time to be afraid of the sunset. Dawn breaks in a blink(13).  累乗の位置に13が
05. An enigma hangs between us. The event horizon was seen only by you.
06. I cannot tell you everything. You of all people should understand why.
07. Let's speak together in one universal language.
08. I have seven, and you have six. I hope you understand my tricks?  何故はてなで終わる
09. Now you've found my path. Traverse its distance with both eyes open.
10. I look forward to our sideways gossip of life's unravelings.
11. I greatly value all you've done, and proudly call you friend.
"""

for s in str.split('\n'):
    #print(g_decode(s))
    print(g_encode(s))

S = """
◆] .}_
19i 2 >
2NNb3'tSS
Hr xxvS
"""
for s in S.split('\n'):
    print(g_decode(s))

S = "the answer you seek in the sum oe your journey to the horizon and to the stars you will find in the remains of the longest path and the dexth of the ocean"
print(g_encode(S))
S = """
¢½ 1|áq A
"""
def g_decode_p(S):
    for s in S:
        tmp = ord(s) - 13
        if tmp < 60: tmp = tmp % 60
        print(tmp , end=",")
    #return [encode_map[s.lower()] for s in S].join("")
for s in S.split('\n'):
    g_decode_p(s)

def both(s, n=1):
    print("%s => decode(-13):%s, encode(+13):%s" % (
        s, g_decode(s, n), g_encode(s))
    )
both('3')
both('P')
both('0')

both('backrub')
both('Flutter')
both('Seven')
both('Six')


S= """
Transmission received: prepare for decoding 
****************************************************************************************************
Files received:
Transmission time: 2993.919ms

Error encountered: files corrupted
Â¢Â½Ã¯1|Ã¡Â¶Â¾A
-+mÂ³rÂ©>$\ÃŒÃÃœ;
ÃÂ«Ã—Ã•\Â¹Âº8jÃ…Ã‡Ã¬+
Â£?ÃÃ¸ÃºÂ²B-
hjzÃ¹EÃ·Ã•] .}_
Â¡/l
1Ã¿Â¡Â½2Â¨>
ï¿½ï¿½ï¿½ï¿½2ï¿½NNb3'ï¿½-ï¿½ï¿½ï¿½t,ï¿½Åžï¿½aï¿½ï¿½$
                         ï¿½Hrï¿½ï¿½ï¿½^-'ï¿½^]xxvS
ï¿½ï¿½Xtï¿½ï¿½rï¿½vï¿½Zï¿½@ï¿½ï¿½ï¿½xWqï¿½ï¿½ï¿½ï¿½ï¿½Jï¿½vÅ|Nï¿½ï¿½:ï¿½>ï¿½ï¿½:ï¿½R)Lï¿½ï¿½
                                            ï¿½
                                             ï¿½ï¿½ï¿½ï¿½qï¿½3ï¿½ï¿½Fï¿½ï¿½ï¿½$ï¿½ï¿½.ï¿½;qï¿½ï¿½jï¿½ï¿½rï¿½Oï¿½ï¿½VGï¿½iï¿½ï¿½Aï¿½{ï¿½ï¿½ï¿½}ï¿½S@ï¿½/ï¿½Oï¿½5ï¿½ï¿½#ï¿½ï¿½Jhï¿½ï¿½ï¿½8$aï¿½ï¿½ï¿½e@$\ejï¿½)ï¿½FCï¿½Q*ï¿½ï¿½ï¿½
                                         zmï¿½qySï¿½ï¿½ï¿½ï¿½?ÆŠï¿½^ï¿½ï¿½ï¿½}ï¿½ï¿½ï¿½tWÚŠï¿½Vï¿½Ö¡Ä¦Xï¿½:ï¿½Û©ï¿½ï¿½\*ï¿½^ ï¿½dï¿½ï¿½L8ï¿½ï¿½1waiting..........
74686520616e7377657220796f75207365656b20696e207468652073756d206f6620796f7572206a6f75726e657920746f2074686520686f72697a6f6e20616e6420746f2074686520737461727320796f752077696c6c2066696e6420696e207468652072656d61696e73206f6620746865206c6f6e67657374207061746820616e6420746865206465707468206f6620746865206f6365616e
hdï¿½ï¿½ï¿½Ë¼ï¿½Xï¿½ï¿½ï¿½j{ï¿½ï¿½ï¿½r    ï¿½ï¿½ï¿½Rï¿½-Jï¿½|i>a-'ï¿½Sï¿½GBï¿½|qï¿½ [ï¿½ï¿½!ï¿½gï¿½$J6Lï¿½ï¿½ï¿½Oï¿½ï¿½K
"""

# for s in S.split('\n'):
#     g_decode(s)

S = "Â¢Â½Ã¯1|Ã¡Â¶Â¾A"
print(g_decode(S))
print(g_encode(S))

S = "-+mÂ³rÂ©>$\ÃŒÃÃœ;"
print(g_decode(S))
print(g_encode(S))

S = "ÃÂ«Ã—Ã•\Â¹Âº8jÃ…Ã‡Ã¬+"
print(g_decode(S))
print(g_encode(S))

S = "Â£?ÃÃ¸ÃºÂ²B-"
both(S)
S = "hjzÃ¹EÃ·Ã•] .}_"
both(S)
S = "Â¡/l"
both(S)
S = "1Ã¿Â¡Â½2Â¨>"
both(S)

both("ï¿½ï¿½ï¿½ï¿½2ï¿½NNb3'ï¿½-ï¿½ï¿½ï¿½t,ï¿½Åžï¿½aï¿½ï¿½$",1)

S="74686520616e7377657220796f75207365656b20696e207468652073756d206f6620796f7572206a6f75726e657920746f2074686520686f72697a6f6e20616e6420746f2074686520737461727320796f752077696c6c2066696e6420696e207468652072656d61696e73206f6620746865206c6f6e67657374207061746820616e6420746865206465707468206f6620746865206f6365616e"
print(sol(S))

both("xxvS",2)

both("Aleuas")
both("google.stanford.edu")
both("tricks")

S = """
¢½ï1|á¶¾A
-+m³r©>$\ÌÐÜ;
Ï«×Õ\¹º8jÅÇì+
£?Íøú²B-
hjzùE÷Õ] .}_
¡/l
1ÿ¡½2¨>
����2�NNb3'�-���t,�Ş�a��$
                         �Hr���^-'�^]xxvS
��Xt��r�v�Z�@���xWq�����J�vŐ|N��:�>��:�R)L��
                                            �
                                             ����q�3��F���$��.�;q��j��r�O��VG�i��A�{���}�S@�/�O�5��#��Jh���8$a���e@$\ej�)�FC�Q*���
                                         zm�qyS����?Ɗ�^���}���tWڊ�V�֡ĦX�:�۩��\*�^ �d��L8��1waiting..........
74686520616e7377657220796f75207365656b20696e207468652073756d206f6620796f7572206a6f75726e657920746f2074686520686f72697a6f6e20616e6420746f2074686520737461727320796f752077696c6c2066696e6420696e207468652072656d61696e73206f6620746865206c6f6e67657374207061746820616e6420746865206465707468206f6620746865206f6365616e
hd���˼�X���j{���r    ���R�-J�|i>a-'�S�GB�|q� [��!�g�$J6L���O��K
"""
print("%s" % ('='*64))
both("¢½ï1|á¶¾A")
both("-+m³r©>$\ÌÐÜ;")
both("Ï«×Õ\¹º8jÅÇì+")
both("£?Íøú²B-")
both("hjzùE÷Õ] .}_")
both("¡/l")
both("1ÿ¡½2¨>")
both("����2�NNb3'�-���t,�Ş�a��$")
both("�Hr���^-'�^]xxvS")
both("��Xt��r�v�Z�@���xWq�����J�vŐ|N��:�>��:�R)L��")
both("�")
both("����q�3��F���$��.�;q��j��r�O��VG�i��A�{���}�S@�/�O�5��#��Jh���8$a���e@$\ej�)�FC�Q*���")
both("zm�qyS����?Ɗ�^���}���tWڊ�V�֡ĦX�:�۩��\*�^ �d��L8��1waiting..........")
both("74686520616e7377657220796f75207365656b20696e207468652073756d206f6620796f7572206a6f75726e657920746f2074686520686f72697a6f6e20616e6420746f2074686520737461727320796f752077696c6c2066696e6420696e207468652072656d61696e73206f6620746865206c6f6e67657374207061746820616e6420746865206465707468206f6620746865206f6365616e")
both("hd���˼�X���j{���r    ���R�-J�|i>a-'�S�GB�|q� [��!�g�$J6L���O��K")
print("%s" % ('='*64))

ul = [
    ['L', ' ', 'E', ' ', 'T', ' ', 'S', ' ', 'S'],
    [' ', 'P', ' ', 'E', ' ', 'A', ' ', 'K', ' ', 'I'],
    ['N', ' ', 'A', ' ', 'U', ' ', 'N', ' ', 'I'],
    [' ', 'V', ' ', 'E', ' ', 'R', ' ', 'S', ' ', 'A'],
    ['L', ' ', 'L', ' ', 'A', ' ', 'N', ' ', 'G'],
    [' ', 'A', ' ', 'U', ' ', 'G', ' ', 'E', ' ', ' ']
]

for n in range(13, 14, 1):
    clue = ul.copy()
    for i, row in enumerate(clue):
        for j, s in enumerate(row):
            if s != ' ':
                clue[i][j] = g_decode(s)

    for row in clue:
        print(row)


import math
def dist(A, B):
    x1, y1 = A
    x2, y2 = B
    tmp = abs(x1 - x2)**2 + abs(y1 - y2)**2
    return math.sqrt(tmp)

def get_slope(A, B):
    x1, y1 = A
    x2, y2 = B
    if x2-x1 == 0:
        return 0 # 垂直の傾きは0でしょ。
    else:
        return (y2-y1) / (x2-x1)


def get_intercept(A, B):
    slope = get_slope(A, B)
    x1, y1 = A
    x2, y2 = B
    #y = ax + b
    b = y1 - slope*x1
    return b

def get_horizon(A, B):
    x1, y1 = A
    x2, y2 = B
    slope = get_slope(A, B)
    intercept = get_intercept(A, B)
    #0 = ax + b
    #ax = -b / a
    if slope != 0:
        x = -(intercept) / slope
    else:
        x = -(intercept)
    xL = max(x1, x2)
    xS = min(x1, x2)
    if xS <= x and x <= xL:
        return (x, 0)
    else:
        return None



print(dist((18, -20), (-4, 19)))
print(dist((-7, -1), (-23, 21)))
print(dist((-15, -18), (-33, 10)))
print(dist((-23, 9), (28, 10)))
print(dist((35, 8), (-36, 19)))

"""
main.bundle.js:1 Transmission Error: 
sendTransmission(
  points: Array<[number, number]>, t: number
) 
did not resolve with [[1,0],[1,0],[1,0],[1,0],[1,0],[1,0]], .123
"""




graph = [
    [(-36, 19), (-41, 9), (-37, -3), (-37, 2), (-25, 16)],          # (-34, 19)
    [(-33, 10), (-29, 11), (-33, 2), (-28, 6), (-29, 9), (-23, 9)],
    [(-23, -21), (-20, -15), (-8, -8), (-15, -18)],                 # (-24, -16) no edge, (-26, 15) no even a dot
    [(-4, 19), (-10, 5), (9, 11), (-6, 15), (-1, 6), (4, 12), (0, 20), (13, 9), (-7, -1)],
    [(27, -4), (24, -15), (24, -8), (24, -12), (24, -17), (18, -20)],
    [(28, 10), (31, 4), (39, 9), (33, 10), (24, 8), (29, 15), (34, 6), (35, 8)] # (32, 12) # no edge
]

class Stars:
    def __init__(self, stars, reversed=False):
        self.stars = stars.copy()
        self.reversed = reversed
        if self.reversed:
            self.stars.reverse()
    def __str__(self):
        return ",".join(self.stars)



def get_stars_in_remains(A, B, graph, gosa=0.5):
    slope = get_slope(A, B)
    intercept = get_intercept(A, B)
    stars_in_remains = []
    for row in graph:
        for star in row:
            x, y = star
            ans = slope * x + intercept
            # 本当だっtら y == slope * x + intercept としたいんだが
            # それだと通る点がなかったので、丸の大きさがだいたい0.5くらい
            # と思うので誤差内かと言う判定に切り替えた
            if ans - gosa <= y and y <= ans + gosa:
                stars_in_remains.append(star)
    return list(set(stars_in_remains).difference(set([A, B])))

def depth_in_ocean(stars_in_remains):
    depth = 0
    for star in stars_in_remains:
        x, y = star
        if abs(x) <= 17 and abs(y) <= 17: # in ocean
            depth += y
    return depth

#

from termcolor import colored
from typing import List
def traverse(cosmos: List[Stars]):
    longest = 0
    longest_points = None
    pre_stars: Stars = None
    points = []
    ttl = 0
    logging.debug("traversing %s" % cosmos)
    for stars in cosmos:
        #コスモス６個与えられたときは一つ目とする
        #points.append(stars.stars[0])
        #コスモス３個与えられたときは最初と最後する
        points.append(stars.stars[0])
        points.append(stars.stars[-1])
        if pre_stars:
            distance = dist(pre_stars.stars[-1], stars.stars[0])
            logging.debug("dist from %s to %s is %s" % (pre_stars.stars[-1], stars.stars[0], distance))
            if distance > longest:
                longest = distance
                longest_points = (pre_stars.stars[-1], stars.stars[0])
            x_cord = get_horizon(pre_stars.stars[-1], stars.stars[0])
            if x_cord:
                journey_horizon = dist(pre_stars.stars[-1], x_cord)
                logging.debug("journey_horizon, from %s to %s through %s is %s" % (pre_stars.stars[-1], stars.stars[0], x_cord, journey_horizon))
                ttl += journey_horizon
        pre_stars = stars

    logging.debug("longest path is from %s to %s it's dist is %s" % (longest_points[0], longest_points[1], longest))
    stars_in_remains = get_stars_in_remains(longest_points[0], longest_points[1], graph)
    if stars_in_remains:
        logging.error("//%s are %s" % (colored("stars_in_remains", "red"), stars_in_remains))
        depth = depth_in_ocean(stars_in_remains)
        logging.error("//sum of depth_in_ocean, from %s to %s is %s" % (longest_points[0], longest_points[1], depth))
        ttl += depth
        logging.error("%s(%s, %s)" % ("sendTransmission", [[x, y] for x, y in points], ttl))
    else:
        logging.warn("%s(%s, %s)" % ("sendTransmission", [[x, y] for x, y in points], ttl))
    return ttl


paths = [
    ((4, False), (3, False), (2, False), (1, False), (5, False), (0, False)),
    ((4, False), (3, False), (2, False), (1, False), (5, True), (0, False)),
    ((4, False), (3, False), (2, False), (1, False), (5, True), (0, False)),
    ((4, False), (3, False), (2, False), (1, False), (5, True), (0, True)),
    ((0, False), (1, False), (2, False), (3, False), (4, False), (5, False))
]


aa = [[0, False], [1, False], [2, False], [3, False], [4, False], [5, False]]
def rec(S, i, chosen):
    ans = []
    if i == len(S):
        #print(chosen)
        return [chosen]
    else:
        #print("%s, %s, %s, %s" % (type(chosen), chosen, S[i], S[i][0]))
        A = chosen.copy()
        A.append([S[i][0], True])
        print("A is %s" % A)
        B = chosen.copy()
        B.append([S[i][0], False])
        print("B is %s" % B)
        ans.extend( rec(S, i+1, A ) )
        ans.extend( rec(S, i+1, B ) )
        return ans

patterns = rec(aa, 0, [])
print("num of patterns is %s , i guess 64" % len(patterns))

print("%s" % ('='*64))
#logging.basicConfig(level=logging.DEBUG, format="%(message)s")
#logging.getLogger().setLevel(logging.INFO)
logging.getLogger().setLevel(logging.ERROR)
for path in paths:
    xxx = [Stars(graph[index], reversed) for index, reversed in path]
    traverse(xxx)

for path in patterns:
    #print(path)
    xxx = [Stars(graph[index], reversed) for index, reversed in path]
    traverse(xxx)
# [Stars(graph[4], False), Stars(graph[3], False), Stars(graph[2], False),
#  Stars(graph[1], False), Stars(graph[5], False), Stars(graph[0], False)]
print("%s" % ('='*64))

both("de castel")
both("I have seven, and you have six")
both("I HAVE SEVEN, AND YOU HAVE SIX")


indices = [0, 1, 2, 3, 4, 5]
for i in indices:
    for j in indices:
        if j == i: continue
        for k in indices:
            if k == i or k ==j: continue
            #print(i, j, k)
            for l in (True, False):
                for m in (True, False):
                    for n in (True, False):
                        traverse([Stars(graph[i], l), Stars(graph[j], m), Stars(graph[k], n)])

