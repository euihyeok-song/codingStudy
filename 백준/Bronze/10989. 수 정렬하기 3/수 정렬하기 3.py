import sys

input = sys.stdin.readline

N = int(input().rstrip())
arr = [0] * 10001

# append를 사용하면 메모리 재할당이 이루어 지면서 메모리를 더 잡아먹음
for i in range(N):
    arr[int(input().rstrip())] += 1
    
for idx, val  in enumerate(arr):
    if val > 0:
        while val != 0:
            print(idx)
            val -= 1

    