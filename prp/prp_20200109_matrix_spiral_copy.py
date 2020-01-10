#--- candidate code (start) ---
def spiral_copy(inputMatrix):
    left, top = 0,0
    right = len(inputMatrix[0])-1# 4
    bottom = len(inputMatrix)-1 #0
    result = []

    while( left <= right and top < bottom ):
        for i in range(left, right):
            result.append(inputMatrix[top][i])
        for i in range(top, bottom):
            result.append(inputMatrix[i][right])
        for i in range(right, left, -1):
            result.append(inputMatrix[bottom][i])
        for i in range(bottom, top, -1):
            result.append(inputMatrix[i][left])
        left += 1
        top += 1
        right -= 1
        bottom -= 1
    if(top == bottom ):
        for i in range(bottom, top, -1):
            result.append(inputMatrix[i][left])
    return result

inputMatrix  = [ [1] ]

a = spiral_copy(inputMatrix)
print(a)
#--- candidate code (end) ---




arrow = {
    0 : ( 1,  0), # right
    1 : ( 0,  1), # down
    2 : (-1,  0), # left
    3 : ( 0, -1), # upa
}
def get_next_direction(idx):
    idx += 1
    if idx > 3: idx = 0
    return idx, arrow[idx],

def spiral_copy(inputMatrix):
    n = len(inputMatrix)
    m = len(inputMatrix[0])
    visited = [[0] * m for _ in range(n)]
    direct_idx = 0 # left
    direct = arrow[direct_idx]
    row = col = 0
    A = []
    def valid(i, j):
        if i < 0 or i >= n: return False
        if j < 0 or j >= m: return False
        return True
    def is_visited(i, j):
        if not valid(i, j): return False
        return visited[i][j] == 1

    while True:
        if not valid(row, col) or visited[row][col]:
            break
        else:
            if visited[row][col] == 0:
                val = inputMatrix[row][col]
                A.append(val)
                visited[row][col] = 1
            else:
                # shold be the last element
                break
        # once I  hit the wall,
        if not valid(row + direct[1], col + direct[0]) or \
            is_visited(row + direct[1], col + direct[0]):
            direct_idx, direct = get_next_direction(direct_idx)
        row += direct[1]
        col += direct[0]
    return A



#
inputMatrix  = [ [1,    2,   3,  4,    5],
                 [6,    7,   8,  9,   10],
                 [11,  12,  13,  14,  15],
                 [16,  17,  18,  19,  20] ]
ret = spiral_copy(inputMatrix)
print(ret)

# test-case1
inputMatrix  = [ [1,    2,   3,  4,    5] ]
ret = spiral_copy(inputMatrix)
print(ret)


# test-case1
inputMatrix  = [ [1] ]
ret = spiral_copy(inputMatrix)
print(ret)

### four wall indices
# top, bottom
# left, right
# (i meets right) you go down
# (j meets bottom) you go left
# (i meets left) you go up
