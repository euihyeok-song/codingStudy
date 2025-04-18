def solution(n, left, right):
    
    num = [0] * (right-left+1)
    
    for idx in range(left,right+1):
        row, col = idx // n, idx % n
        num[idx-left] = max(row,col) + 1
    
    return num