N = int(input())

array = [[0]*N for _ in range(N)]
total = 0

for i in range(N):
    
    array[i] = list(map(int,input().split(' ')))
    
# 수열의 전체 합 구하기 ()
for j in range(N):
    
    total += sum(array[j])
    
total = int(total / (2 * (N-1)))

# A[0] + A[1] + .. + A[N-1]

if N > 2:
    a = int((sum(array[0][:]) - total) / (N-2))
else:
    a = int(total / 2)

for k in range(N):
    
    if k == 0:
        print(a, end=' ')
    elif k == N-1:
        print(array[0][-1]-a)
    else:
        print(array[0][k] - a, end=' ')
