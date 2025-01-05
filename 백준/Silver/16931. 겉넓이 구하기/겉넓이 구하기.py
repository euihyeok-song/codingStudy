N, M = map(int, input().split(' '))

array = [list(map(int, input().split(' '))) for _ in range(N)]

left = 0        
# 오른쪽 , 왼쪽 (둘다 동일)
for i in range(N):
    for j in range(M):
        
        if j == 0:
            left += array[i][j]
        else:
            if array[i][j-1] < array[i][j]:
                left += array[i][j] - array[i][j-1]
# 오른쪽, 왼쪽 둘다 계산
left *= 2

front = 0
# 앞쪽, 뒷쪽 (둘다 동일)
for k in range(M):
    for l in range(N):
        
        if l == 0:
            front += array[l][k]
        else:
            if array[l-1][k] < array[l][k]:
                front += array[l][k] - array[l-1][k]
# 앞쪽, 뒷쪽 둘다 계산
front *= 2

print(left + front + 2*N*M)