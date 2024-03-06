# 연속합 - 메모리초과 발생(2차원 말고 1차원으로 만들어보기)

# 수열의 총 갯수
n = int(input())

# 입력받은 수열
A = list(map(int,input().split()))

for i in range(1,n):
    A[i] = max(A[i],A[i-1]+A[i])
    
print(max(A))
    