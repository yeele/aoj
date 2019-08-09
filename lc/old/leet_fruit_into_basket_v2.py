#-*- coding: utf-8 -*-
class Solution:
    def totalFruit(self, tree):
        """
        :type tree: List[int]
        :rtype: int

# when baskets is larger than 2.
# keep last char, remove rest.
baskets = {
  # v: idx
    3: 2
    1: 3
}


[3,3,3,1,2,1,1,2,3,3,4]
       i
         j

[0,1,2,2]
 i
 j

[1,2,3,2,2]
   i
     j


[1,0,1,4,1,4,1,2,3]
 i
       j
"""
        i = j = 0  # i:0, j:0
        bskt = {}
        ans = 0
        while j < len(tree):  # j:3 < 9
            value = tree[j] # j:3, value:4
            if  len(bskt) < 2 or value in bskt.keys():
                # add
                bskt[value] = j # bskt = {1:2, 0:1}
            else:
                bskt[value] = j   # bskt = {1:2, 0:1, 4:3}
                baskets = (value, tree[j-1])
                # shift i window
                i = j
                while tree[i] in baskets:
                    i-=1
                # i points to out of basket
                del bskt[tree[i]] # bskt = {}
                i+=1

            # evaluate
            ans = max(ans, j-i+1) # i:0, j:2 => ans:3
            j+=1 # j:2 + 1 => j:3
        return ans