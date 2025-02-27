import sys

input = sys.stdin.readline

N = int(input().rstrip())
arr = []
cnt = []

for i in range(N):
    arr.append(int(input()))

arr.sort()
    
for j in arr:
    if not cnt:
        cnt.append([j,1])
        continue

    if j == cnt[-1][0]:
        cnt[-1][1] += 1
    else:
        cnt.append([j,1])
        
cnt.sort(key=lambda x: x[:][1],reverse=True)

print(cnt[0][0])