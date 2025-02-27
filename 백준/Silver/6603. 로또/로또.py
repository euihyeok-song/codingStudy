import sys

input = sys.stdin.readline

def backtracking(start):
    
    if len(check) == 6:
        print(*check)
        return
    
    for i in range(start,N):
        check.append(ans[i])
        backtracking(i+1)
        check.pop()

while True:
    
    ans = list(map(int, input().rstrip().split(' ')))
    N = len(ans)

    if ans[0] == 0:
        break
        
    visited = [False] * (ans[0] + 1)
    result = []
    check = []

    backtracking(1)
    print()