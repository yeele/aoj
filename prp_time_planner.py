"""
a = set(list(range(a1, a2 + 1)))
b = set(list(range(b1, b2 + 1)))
"""

def within(a, x, y):
    #return if a is in between
    return x <= a and a <= y

def meeting_planner(slotsA, slotsB, dur):
    # O(N * M)
    # O(min(N, M))
    for (a1, a2) in slotsA:
        for (b1, b2) in slotsB:
            b_expected_end = b1 + dur
            print(a1, a2, b1, b2)
            if a1 <= b_expected_end and b_expected_end <= a2:
                if a1 <= b1 and b1 <= a2:
                    if b_expected_end <= b2:
                        return [b1, b_expected_end]
    return []



def test_case1():
    slotsA = [[10, 50], [60, 120], [140, 210]]
    slotsB = [[0, 15], [60, 70]]
    dur = 8
    return (slotsA, slotsB, dur)

def test_case2():
    slotsA = [[10, 50], [60, 120], [140, 210]]
    slotsB = [[0, 15], [60, 70]]
    dur = 12
    return (slotsA, slotsB, dur)

if __name__ == "__main__":
    (slotsA, slotsB, dur) = test_case1()
    ret = meeting_planner(slotsA, slotsB, dur)
    print(ret)
