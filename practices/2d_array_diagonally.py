

b = 5
S = [[0]*b for i in range(b)]
for i in range(b):
    for j in range(5):
        S[i][j] = b * i + j
for s in S:
    print(s)



print("loop horizontally")
for s in S:
    for o in s:
        print(o, end=",")

print()
print("loop vertically")
for r in range(len(S)):
    for c in range(len(S)):
        print(S[c][r], end=",")

print()
print("loop diagonally")
for i in range(len(S)):
    for r in range(len(S)):
        for c in range(r, len(S)):
            try:
                print(S[r][c+i], end=",")
            except:
                pass
            break

# loop hintted by
# https://leetcode.com/problems/longest-palindromic-substring/discuss/297375/Python-easy-to-understand-DP-solution

print()
print("loop diagonally wiht for and while")
for offset in range(len(S)):
    r = 0
    c = 0 + offset
    while r < len(S) and c < len(S):
        print(S[r][c], end=",")
        r+=1
        c+=1

print()

