"""
Question: Given a stack, sort the elements in the stack using one additional stack.
eg.
sort([1, 3, 2, 4]) = [1, 2, 3, 4]
Solution: https://www.byte-by-byte.com/sortstacks/
"""

"""
bubble, selection, insertion sO(1)
Merge sort -> recursion and stack(logN) + 1 stack
Quick sort ->  
"""

def mergesort(S):
    """
    [1, 2, 3, 4]
     i           j
    """
    def merge(S, T):
        U = []
        i,j = 0, 0
        while i < len(S) or j < len(T):
            if i >= len(S):
                U.append(T[j])
                j += 1
            elif j >= len(T):
                U.append(S[i])
                i += 1
            else:
                if S[i] < T[j]:
                    U.append(S[i])
                    i += 1
                else:
                    U.append(T[j])
                    j += 1
        return U

    def rec(S, i, j):
        if j - i == 1:
            return S[i:j]

        m  = (j - i) // 2 + i
        left = rec(S, i, m)
        right = rec(S, m, j)
        ret = merge(left, right)
        return ret

    return rec(S, 0, len(S))


print(mergesort([1, 3, 9, 2]))
print(mergesort([1, -3, 9, 0, 2, 1]))
