import sys

input = sys.stdin.readline

N = int(input().rstrip())
arr = [0] * N

for i in range(N):
    arr[i] = int(input().rstrip())
    
for j in sorted(arr):
    print(j)