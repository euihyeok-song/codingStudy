def solution(num_list):
    answer = 0
    
    for val in num_list:
        
        while(val != 1):
            # 짝수일 경우
            if(val % 2 == 0):
                val /= 2
            else:
                val = (val-1)/2
            answer += 1
    
    # 모범 코드 => 2진수에서는 Ob11010과 같이 나오는데 1을 남기려면 ob와 마지막 수를 제외하고
    # 모두 삭제시켜야 하는데, 이는 2로 나눈 횟수와 동일
    # answer = sum(len(bin(i)) - 3 for i in num_list)
    
    return answer