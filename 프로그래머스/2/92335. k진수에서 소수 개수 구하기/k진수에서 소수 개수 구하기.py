def check_prime(x):
    
    if x == 1:
        return False
    
    for i in range(2,int(x**0.5)+1):
        if x % i == 0:
            return False
    
    return True
        

def solution(n, k):
    cnt,num = 0, ''
    base, answer = [], []
    
    # 진수 구하기
    while n >= k:
        base.append(str(n%k))
        n //= k
    base.append(str(n))
    base.reverse()
    
    # 0 제거
    for val in base:
        if val != '0':
            num += val
        else:
            if num != '':
                answer.append(num)
            num = ''
    
    if num != '':
        answer.append(num)
        
    # 소수 찾기
    for x in answer:
        if check_prime(int(x)):
            cnt += 1
    
    return cnt