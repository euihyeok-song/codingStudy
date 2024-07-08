def solution(arr, queries):
    answer = []
    
    # 아래는 너무 cost가 많이 드는 코드
    # answer = [-1] * len(queries)
    # for idx, val in enumerate(queries):
    #     min = 1000000
    #     for i in range(val[0],val[1]+1):
    #         if(arr[i] > val[2] and arr[i] < min):
    #             min = arr[i]
    #             answer[idx] = min
    
    # min함수를 써서 다시 짠 코드
    for a,b,c in queries:
        tmp = []
        for idx in range(a,b+1):
            if(arr[idx] > c):
                tmp.append(arr[idx])
        # tmp가 비어있는 경우를 생각해서 조건문으로 넣어줘야 함
        answer.append(-1 if not tmp else min(tmp)) 
        
    return answer