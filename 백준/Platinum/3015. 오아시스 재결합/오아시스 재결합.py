import sys

input = sys.stdin.readline

N = int(input())
cnt = 0
stack = []

for _ in range(N):
    height = int(input())
    same = 1  # 현재 키를 가진 사람의 개수

    # 스택에서 자신보다 작거나 같은 키 제거
    while stack and stack[-1][0] <= height:
        cnt += stack[-1][1]  # 해당 그룹의 사람들은 전부 볼 수 있음
        if stack[-1][0] == height:
            same += stack[-1][1]  # 같은 키가 연속되면 그룹화
        stack.pop()

    # 스택에 현재 키 추가
    if stack:
        cnt += 1  # 바로 앞의 사람과는 무조건 볼 수 있음
    
    stack.append([height, same])

print(cnt)
