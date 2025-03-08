import sys

input = sys.stdin.readline

N,r,c = map(int, input().rstrip().split(' '))

def func(x, y, length, cnt):
    
    if length == 1:  # 더 이상 쪼갤 수 없는 경우, 정답 출력
        print(cnt)
        exit()
    
    half = length // 2  
    
    # 제 1사분면 (좌상)
    if x < half and y < half:
        func(x, y, half, cnt)
    # 제 2사분면 (우상)
    elif x < half and y >= half:
        func(x, y - half, half, cnt + half * half)
    # 제 3사분면 (좌하)
    elif x >= half and y < half:
        func(x - half, y, half, cnt + 2 * half * half)
    # 제 4사분면 (우하)
    else:
        func(x - half, y - half, half, cnt + 3 * half * half)
    
func(r,c,2**N,0)