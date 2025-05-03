from collections import deque

cnt = 0

def dfs(numbers,idx,result,target):
    
    global cnt
    
    if idx < len(numbers):
        curr = numbers[idx]
        dfs(numbers, idx+1, result+curr, target)
        dfs(numbers, idx+1, result-curr, target)
    else:
        if result == target:
            cnt += 1
    

def solution(numbers, target):
    
    dfs(numbers,0,0,target)
    
    return cnt