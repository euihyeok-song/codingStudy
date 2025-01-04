# 시간 제한이 0.5초이기 떄문에, 1 <= N <= 1,000,000 이므로 for문은 1번만 가능

import sys

N = int(sys.stdin.readline())

total = 0

# for문을 2번쓰는 경우 (시간 초과)
# for i in range(1,N+1):
#     for j in range(1,i+1):
#         if i % j == 0:
#             total += j


# for문을 1번쓰는 경우
# 각 배수들이 총 몇번 들어가는지 생각하자
for i in range(1,N+1):
    total += i * (N//i)


print(total)