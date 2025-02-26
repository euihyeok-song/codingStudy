import sys

input = sys.stdin.readline

N, S = map(int,input().rstrip().split(' '))

element = list(map(int,input().rstrip().split(' ')))
cnt = 0

def backtracking(idx, num):
    
    global cnt
    
    if idx == N:
        return
    
    num += element[idx]
    
    if num == S:
        cnt += 1

    # 숫자 포함
    backtracking(idx+1, num)
    # 숫자 미포함
    backtracking(idx+1, num - element[idx])

backtracking(0, 0)
print(cnt)