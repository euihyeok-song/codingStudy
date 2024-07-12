def solution(arr):
    answer = [[]]
    row = len(arr)              # row는 행
    col = len(arr[0])           # col는 열
    
    answer = arr
    if(row > col):
        for _ in range(row-col):
            for i in range(row):
                answer[i].append(0)
    elif(row < col):
        for j in range(col-row):
            answer.append([0]*col)
        
    
    return answer