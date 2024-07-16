def solution(arr, divisor):
    answer = []
    
    for val in arr:
        if val % divisor == 0:
            answer.append(val)
        
    # 앞의 부분이 false일 경우에 뒤에 부분이 출력됨    
    return sorted(answer) or [-1]