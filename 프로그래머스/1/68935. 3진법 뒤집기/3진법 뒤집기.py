def solution(n):
    answer = 0
    three = []
    
    # 3진법으로 만들기
    while(n != 0): 
        
        three.append(n%3)
        n //= 3
        
    three.reverse()
    
    for i in range(len(three)):
        answer += three[i] * (3**i)
    
    return answer