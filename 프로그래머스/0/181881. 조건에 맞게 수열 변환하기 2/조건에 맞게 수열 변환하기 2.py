def solution(arr):
    answer = 0
    last = [0]*len(arr)
    
    while(1):
        
        for i in range(len(arr)):
            last[i] = arr[i]
            
        for idx,val in enumerate(arr):
            if(val >= 50 and val % 2 == 0):
                arr[idx] = int(arr[idx] / 2)
            elif(val < 50 and val % 2 == 1):
                arr[idx] = arr[idx] * 2 + 1
        
        if last == arr:
            break
        else:
            answer += 1
    
    return answer