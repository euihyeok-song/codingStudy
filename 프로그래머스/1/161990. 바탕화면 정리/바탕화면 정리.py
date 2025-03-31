def solution(wallpaper):
    rows, cols = len(wallpaper), len(wallpaper[0])
    min_row, min_col = rows, cols
    max_row, max_col = 0, 0
    
    for r in range(rows):
        for c in range(cols):
            if wallpaper[r][c] == "#":
                min_row = min(min_row, r)
                min_col = min(min_col, c)
                max_row = max(max_row, r)
                max_col = max(max_col, c)
    
    return [min_row, min_col, max_row + 1, max_col + 1]
