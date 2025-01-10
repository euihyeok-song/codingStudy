def dfs(x, y, number):
    if len(number) == 6:
        if number not in result:
            result.append(number)
        return
        
    dx = [1, -1, 0, 0] 
    dy = [0, 0, 1, -1]
    
    for idx in range(4):
        ndx = x + dx[idx]
        ndy = y + dy[idx]
        
        if 0 <= ndx < 5 and 0 <= ndy < 5:
            dfs(ndx, ndy, number + digit[ndx][ndy]) 

digit = [list(map(str, input().split())) for _ in range(5)]

result = []

for i in range(5):
    for j in range(5):
        dfs(i, j, digit[i][j]) 
print(len(result))