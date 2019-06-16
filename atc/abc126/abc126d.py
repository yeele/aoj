#-*- coding: utf-8 -*-
"""
oj dl https://atcoder.jp/contests/abc116/tasks/abc116_d -d test-d
oj test -d test-d -c "python abc116d.py"
oj test -d test-d -c "python abc116d.py" test-d/sample-3.in
"""

from collections import defaultdict
import sys
import time
import logging



def deco(func):
    def wrapper(*args, **kwargs):
        s = time.time()
        #print('--start--')
        ret = func(*args, **kwargs)
        logging.debug('--end in %f --' % (time.time() - s))
        return ret

    return wrapper


def sol(n, k, S):
    logging.debug("n:%s, k:%s, S:%s" % (n, k, S))
    longest = 0
    k_tmp = 0
    C = [] # checkpoint
    def get_length(idx, C, k_tmp, k):
        c_idx = k_tmp - (k+1)
        try:
            c_value = C[c_idx]
        except:
            c_value = 0
        return idx - c_value + 1

    for i in range(len(S)):
        cur_length = get_length(i, C, k_tmp, k)
        logging.debug("i:%s, S[%s]:%s, k_tmp:%s, cur:%s, max:%s, C:%s" % (
            i, i, S[i], k_tmp, cur_length, longest, C)
        )
        longest = max(longest, cur_length)
        if (i > 0 and S[i-1] == '1' and S[i] == '0') or (i == 0 and S[i] == '0'):
            k_tmp += 1
        if i > 0 and S[i] == '1' and S[i-1] == '0':
            C.append(i)
    return longest





do_submit = True
#do_submit = False
if do_submit:
    logging.basicConfig(level=logging.ERROR, format="%(message)s")
else:
    logging.basicConfig(level=logging.DEBUG, format="%(message)s")

def input_parse(input_str):
    lines = [x.strip() for x in input_str.split("\n") if x.strip()]
    parsed_lines = [[x.strip() for x in line.split()] for line in lines]
    n, k = parsed_lines[0]
    n = int(n)
    k = int(k)
    S = parsed_lines[1][0]
    return (n, k, S)


if not do_submit:
    n, k, S = input_parse("""
    14 2
    11101010110011
    """)
    print(sol(n, k, S))

    n, k, S = input_parse("""
    5 1
    00010
    """)
    print(sol(n, k, S))

    n, k, S = input_parse("""
    1 1
    1
    """)
    print(sol(n, k, S))


else:
    str = ""
    str += input().strip() + "\n"# n, k
    str += input().strip() # S
    n, k, S = input_parse(str)
    print (sol(n, k, S))


