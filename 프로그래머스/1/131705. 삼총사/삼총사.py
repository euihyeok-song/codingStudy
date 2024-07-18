from itertools import combinations

def solution(number):
    answer = 0
    
    # for i in range(len(number)-2):
    #     for j in range(i+1,len(number)-1):
    #         for k in range(j+1,len(number)):
    #             if(number[i]+number[j]+number[k] == 0):
    #                 answer += 1
        
    # 모범답안  combinations(배열, 한 그룹에 들어갈 숫자 갯수)
    for i in combinations(number,3):
        if sum(i) == 0:
            answer += 1
    
    return answer