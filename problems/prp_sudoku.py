

def validate(board, row_start, row_end, col_start, col_end):
    # list of numbers
    cache_template = {1:False, 2:False, 3:False, 4:False, 5:False,
                      6:False, 7:False, 8:False, 9:False}
    cache = cache_template[:]
    for r in range(row_start, row_end+1):
        for c in range(col_start, col_end+1):
            number = board[r][c]
            cache[number] = True
    # validate
    return all(cache.values())




def sudoku_solve(board):
    # board is 2 dimentional array
    # validate if answer follows the sudoku rule.
    # board may be filled or not filled with all numbers.
    # 1. checking row is filled with 1-9 but each didgit appear once
    # 2. checking column is filled with 1-9 but each didgit appear once
    # 3. 3x 3 square box also should be filled with 1-9 but each didgit appear once
    cache_template = {1:False, 2:False, 3:False, 4:False, 5:False,
                      6:False, 7:False, 8:False, 9:False}

    for i in range(9): # row number is i
        cache_row = cache_template[:]
        for j in range(9): # columm number is j
            d = board[i][j]
            cache_row[d] = True
        # validate
        if not all(cache_row.values()): return False
    # columns
    for i in range(9): # row number is i
        cache_col = cache_template[:]
        for j in range(9): # columm number is j
            c = board[j][i]
            cache_col[c] = True
        # validate
        if not all(cache_col.values()): return False

    for x in [(0, 2), (3, 5), (6, 8)]:
        for y in [(0, 2), (3, 5), (6, 8)]:
            row_start, row_end = x
            col_start, col_end = y
            ret = validate(board, row_start, row_end, col_start, col_end)
            if not ret: return False

    return True
