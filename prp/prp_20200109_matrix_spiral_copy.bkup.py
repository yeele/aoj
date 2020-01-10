def exist(i, j, inputMatrix, visited):
    print("exit")
    try:
        if inputMatrix[i][j]:
            if visited[i][j] == 0:
                return True
    except:
        return False

def increment(i, j, inputMatrix, visited, direction):
    # direction
    #(di, dj)
    # 0, 1 => going right
    # 1, 0 => going down
    # 0, -1=> going left
    #-1, 0 => going up
    print("increment:i:%s, j:%s, direction:%s" % (i, j, direction))
    if direction == (0, 1):
        if j+1 < len(visited[0]) and visited[i][j+1] ==0:
            return (i, j+1)
        elif j+1 >= len(visited[0]) or visited[i][j+1] ==1:
            return (i+1, j)
        else: return (i, j)
    elif direction == (1, 0):
        if i+1 < len(visited) and visited[i+1][j] ==0:
            return (i+1, j)
        elif i+1 >= len(visited) or visited[i+1][j] ==1:
            return (i, j-1)
        else: return (i, j)
    elif direction == (0, -1):
        if j-1 >=0 and visited[i][j-1] ==0:
            return (i, j-1)
        elif j-1 < 0 or visited[i][j-1] ==1:
            return (i-1, j)
        else: return (i, j)
    elif direction == (-1, 0):
        if i-1 >=0 and visited[i-1][j] ==0:
            return (i-1, j)
        elif i-1 < 0 or visited[i-1][j] ==1:
            return (i, j+1)
        else: return (i, j)
    else:
        print ("bad")
        return (i, j)










def spiral_copy(inputMatrix):
    h = len(inputMatrix)
    w = len(inputMatrix[0])
    visited = [[0]*w for x in range(h)]

    i = j = 0
    pre = True
    ans = []
    pi = 0
    pj = -1
    print("spiral_copy(inputMatrix)" % inputMatrix)
    while True:
        if exist(i, j, inputMatrix, visited):
            # visit
            visited[i][j] = 1
            ans.append(inputMatrix[i][j])
            for x in visited: print(x)
            print(ans)
            (di, dj) = (i-pi, j-pj) # direction
            (pi, pj) = (i, j)
            (i, j) = increment(i, j, inputMatrix, visited, (di, dj))
        else:
            break

    return ans


inputMatrix  = [ [1,    2,   3,  4,    5],
                 [6,    7,   8,  9,   10],
                 [11,  12,  13,  14,  15],
                 [16,  17,  18,  19,  20] ]
ret = spiral_copy(inputMatrix)
print(ret)

### four wall indices
# top, bottom
# left, right
# (i meets right) you go down
# (j meets bottom) you go left
# (i meets left) you go up