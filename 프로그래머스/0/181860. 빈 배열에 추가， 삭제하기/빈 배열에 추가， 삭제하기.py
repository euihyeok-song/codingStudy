def solution(arr, flag):
    answer = []


    
    for idx, val in enumerate(flag):
        
        if(val == True):
            count = 0
            while(count < arr[idx]*2):
                answer.append(arr[idx])
                count += 1
        else:
            count = 0
            while(count < arr[idx]):
                answer.pop()
                count += 1
                
    return answer