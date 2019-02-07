"""
a = set(list(range(a1, a2 + 1)))
b = set(list(range(b1, b2 + 1)))
"""
"""
a = set(list(range(a1, a2 + 1)))
b = set(list(range(b1, b2 + 1)))
"""



def meeting_planner_naivie(slotsA, slotsB, dur):
    # naive soltion # O(n**2)
    # pseudo code
    for (As, Ae) in slotsA:
        for (Bs, Be) in slotsB:
            start = max(As, Bs)
            end = min(Ae, Be)
            if start + dur <= end:
                return [start, start+dur]
    return []


def meeting_planner(slotsA, slotsB, dur):
    # naive soltion # O(n**2)
    # pseudo code
    # fastest O(1) , worst O(2*N) =>. O(N)
    # space: O(1)
    pa = pb = 0
    while pa < len(slotsA) and pb < len(slotsB):
        # if A, B overlaps, evaluate
        (As, Ae) = slotsA[pa] # 10, 50
        (Bs, Be) = slotsB[pb] #  0, 15

        start = max(As, Bs) # 10
        end = min(Ae, Be)   # 15
        print(As, Ae, Bs, Be, start, end, dur)
        if start + dur <= end:  # 10+8 <= 15
            return [start, start+dur]
        # else: increment whiever, start is smaller
        if Ae < Be: pa+=1
        else: pb+=1
        print(pa, pb)
    return []

if __name__ == "__main__":
    slotsA = [[10, 50], [60, 120], [140, 210]]
    slotsB = [[0, 15], [60, 70]]
    dur = 12
    #dur = 8
    ret = meeting_planner(slotsA, slotsB, dur)
    print(ret)


