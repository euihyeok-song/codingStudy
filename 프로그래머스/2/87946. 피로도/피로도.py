result = 0

def dfs(k, cnt, dungeons, visited):
    global result
    if result < cnt:
        result = cnt
    
    for idx in range(len(dungeons)):
        if dungeons[idx][0] <= k and visited[idx] is False:
            visited[idx] = True
            dfs(k-dungeons[idx][1], cnt+1, dungeons, visited)
            visited[idx] = False
    

def solution(k, dungeons):
    
    global result
    visited = [False] * len(dungeons)
    dfs(k, 0, dungeons, visited)
    
    return result