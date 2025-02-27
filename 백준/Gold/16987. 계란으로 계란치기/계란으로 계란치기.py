import sys

input = sys.stdin.readline

N = int(input().rstrip())
egg = []

# 깬 달걀의 갯수
total = 0

for _ in range(N):
    egg.append(list(map(int,input().rstrip().split(' '))))
    
def check(egg):
    
    cnt = 0
    
    for x,_ in egg:
        if x <= 0:
            cnt += 1
    
    return cnt
        

def backtracking(curr):
    
    global total
    
    # 현재를 제외한 모든 달걀 깨졌는지 여부
    all_broken = True
    
    if curr >= N:
        total = max(total,check(egg))
        return
    
    # 전체 계란을 모두 탐색
    for i in range(N):
        
        # 현재 든 계란이 깨진 경우
        if egg[curr][0] <= 0:
            backtracking(curr+1)
        # 깨려고 하는 계란이 이미 꺠진 경우
        elif egg[i][0] <= 0 or i == curr:
            continue
        else:
            all_broken = False
            # 계란 꺠기
            egg[curr][0] -= egg[i][1]
            egg[i][0] -= egg[curr][1]
            backtracking(curr+1)
            egg[curr][0] += egg[i][1]
            egg[i][0] += egg[curr][1]

    # 깨트릴게 없는경우 skip
    if all_broken is True:
        backtracking(curr+1)

# 처음 들고 있는 계란의 index값 넣어줌
backtracking(0)
print(total)