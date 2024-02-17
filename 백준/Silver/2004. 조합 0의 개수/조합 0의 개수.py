# 조합 0의 개수
# 시간초과 발생 해결
# 중요함 -> 10의 배수 구하는 방법
# 0의 개수 구하는 방법 -> 10의 개수 구하기 -> 2의 개수와 5의 개수중 작은 것의 개수

# X!에 포함된 2의 개수 구하기
def two_count(num):
    t_count = 0
    while(num != 0):
        num //= 2
        t_count += num
    return t_count
    
# X!에 포함된 5의 개수 구하기
def five_count(num):
    f_count = 0
    while(num != 0):
        num //= 5
        f_count += num
    return f_count
    
N, M = map(int,input().split())

K = N-M

N_t_count = two_count(N)
N_f_count = five_count(N)
M_t_count = two_count(M)
M_f_count = five_count(M)
K_t_count = two_count(K)
K_f_count = five_count(K)

print(min(N_t_count-M_t_count-K_t_count,N_f_count-M_f_count-K_f_count))