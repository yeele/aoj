def root(x, n):
    if x == 0: return 0
    if x == 1: return 1
    r_min = x if x < 1 else 1
    r_max = 1 if x < 1 else x
    while r_min < r_max:
        mid = (r_min + r_max) / 2.0
        guess = mid ** n
        if guess == x: return mid
        #elif abs(guess-x) <= 0.001: # still works
        elif abs(r_max - r_min) <= 0.001:
            return mid
        elif guess > x:
            # mid should smaller
            # pick the first half
            r_max = mid
        else:
            # mid should bigger
            # pick the first half
            r_min = mid


def root_v2(x, n):
    if x == 0: return 0
    if x == 1: return 1
    r_min = x if x < 1 else 1
    r_max = 1 if x < 1 else x
    while r_min < r_max:
        mid = (r_min + r_max) / 2.0
        guess = mid ** n
        if guess == x: return mid
        elif abs(r_max - r_min) <= 0.001: return mid
        elif guess > x: r_max = mid
        else: r_min = mid

