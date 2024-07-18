def solution(n):
    answer = 0
    three = []
    
#     # 3진법으로 만들기
#     while(n != 0): 
        
#         three.append(n%3)
#         n //= 3
        
#     three.reverse()
    
#     for i in range(len(three)):
#         answer += three[i] * (3**i)

    tmp = ''
    while n:
        tmp += str(n % 3)
        n = n // 3

    # 3진법으로 만들어줌
    answer = int(tmp, 3)
    
    
    return answer