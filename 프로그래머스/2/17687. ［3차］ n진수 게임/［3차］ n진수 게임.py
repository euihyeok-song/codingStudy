def convertTobase(x, n):
    num = "0123456789ABCDEF"
    
    # divmod(a,b)는 (a // b, a % b)을 반환해줌
    q, r = divmod(x, n)
    
    if q == 0:
        return num[r]
    else:
        return convertTobase(q, n) + num[r]

def solution(n, t, m, p):
    total, answer = "", ""
    
    # 최댓값을 만들어 두고 계산 ( m*t 가 최대 )
    for i in range(m*t):
        total += convertTobase(i,n)
        
    for idx,val in enumerate(total):
        if idx % m == (p-1) and t > 0:
            answer += val
            t -= 1
    
    return answer