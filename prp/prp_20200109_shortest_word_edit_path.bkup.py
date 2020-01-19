def rep(s, index, newstring):
    return s[:index] + newstring + s[index + 1:]

def shortestWordEditPath(source, target, words):
    """
      @param source: str
      @param target: str
      @param words: str[]
      @return: int
      """
    """
    BFS
    ["but", "put", "big", "pot", "pog", "dog", "lot"]
    
    bit -> -it, b-t, bi-
    but -> -ut, b-t, bu-
    put -> -ut, p-t, pu-
    
    -ut: [but, put]
    
    ○ -> ○
    
        bit
        -it   b-t   bi-
      NULL   but:
              -ut                         b-t:NULL    bu-:NULL
              put:------x
              -ut:NULL  p-t:
              p-t       
              pot       pot:
                        po-:pog:og->dog VICTORY      
              -ot:
              lot
              l-t: NULL
              -ot: NULL
    depth = 1
    
    seen = {dict of each word} 
    
    recursiveHelper(source, target, seen)
    
    recursiveHelper(source, target, seen):
      if source == target:
        return True
      else:
        for key in lookupKey[word]: #-it, b-t, bi-
          for word in key:
            if word in seen:
              continue
            else:
              seen.add(word)
              if(recursiveHelper(word,target, seen)):
                depth = depth + 1
                return True
              seen.remove(word)
           
    return depth            
        
    
    """
    from collections import defaultdict
    lookup = defaultdict(list)
    links  = defaultdict(list)
    for word in words:
        for i in range(len(word)):
            link = rep(word, i, '-')
            lookup[link].append(word)
            links[word].append(link)
            #print(lookup)
    #print(links)
    #visited = dict([(word, 0) for word in words])
    seen = []
    dep = 0
    def rec(source, target, seen):
        #print(source, target)
        if source == target:
            return True
        else:
            for link in links[word]: # -it, b-t, -it
                for next_word in lookup[link]: # list of words,
                    if (not next_word in seen) or (next_word != word):
                        seen.append(word)
                        ret = rec(next_word, target, seen)
                        if ret: dep += 1
                        seen.remove(word)
                        return ret
    rec(source, target, seen)
    return dep

#print(rep("bit", 1, '-')) # 'b-t'
source = "bit"; target = "dog"
words = ["but", "put", "big", "pot", "pog", "dog", "lot"]
dep = shortestWordEditPath(source, target, words)
print(dep)





'''
Solution: Breadth First Search

Finding a shortest path is typically done with a breadth first search. Here, we have some underlying graph of words, and two words are connected (neighbors) if they differ by exactly one letter (and have the same length).

The breadth first search explores all nodes distance 0 from the source, then all nodes distance 1, then all nodes distance 2, and so on. This ensure that if we find the target word, we found it at the least possible distance and thus the answer is correct.

One difficulty in this question is, given a word, what are all neighboring words? (Words that differ by exactly one letter.)

There are two strategies to enumerating these neighbors:

    One strategy is, for every word2 in the given words, check that word and word2 differ by 1.

    Another strategy is, for every index i from 0 .. word.length - 1 and for every lowercase letter c, clone word into word2, replace word2[i] with c, and check whether the resulting word2 is in words.

The decision to use one strategy or another depends on the input parameters. Here, we showcase the second strategy, with the first in the comments.

===============================


function shortestWordEditPath(source, target, words):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    wordset = new HashSet(words)
    queue = Queue()
    queue.add((source, 0))
    seen = new HashSet([source])

    while queue:
        word, depth = queue.popfront()
        if word == target: return depth
        for i from 0 to word.length:
            # First Strategy:
            # for word2 in words:
            #     if word2.length == word.length:
            #         diff = 0
            #         for j from 0 to word.length:
            #             if word[j] != word2[j]:
            #                 diff += 1
            #                 if diff == 2: break
            #         if diff == 1 and word2 not in seen:
            #             queue.append((word2, depth+1))
            #             seen.add(word2)

            # Second Strategy:
            for c in alphabet:
                word2 = word.clone()
                word2[i] = c
                if word2 in wordset and word2 not in seen:
                    queue.append((word2, depth+1))
                    seen.add(word2)
    return -1
    
'''