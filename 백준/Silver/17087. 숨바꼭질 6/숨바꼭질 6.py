# 숨바꼭질 6
import math

# N은 동생 수 / S는 나으 위치
N , S = map(int,input().split(' '))

# 동생들의 위치
A = list(map(int,input().split(' ')))

distance = []

for i in range(N):
    
    # X+D일 경우는 그냥 거리 계산
    if((S-A[i] > 0)):
        distance.append(S-A[i])
    # X-D일 경우는 절댓값을 씌움(기존 라이브러리 함수에 포함)
    else:
        distance.append(abs(S-A[i]))
    

while(len(distance) > 1):

    X = distance.pop()
    Y = distance.pop()
    
    distance.append(math.gcd(X,Y))
    
print(distance[0])