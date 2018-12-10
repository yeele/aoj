#-*- coding: utf-8 -*-
import random
print("start way to jg19")

a = [random.randint(1, 10) for x in range(100000)]
#a = [6, 10, 5, 4, 1, 8, 7, 10, 7, 2]
print (a)

# what if empty list
# what if single entry
def find_max_profit(a):
    cur_max = 0
    for i, x in enumerate(a):
        for j, y in enumerate(a[i::]):
            cur_max = y - x if y - x > cur_max else cur_max
    return cur_max

print(find_max_profit(a))