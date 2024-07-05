def solution(arr, delete_list):
    answer = []
    
    for i in range(len(arr)):
        flag = 0
        for j in range(len(delete_list)):
            if(arr[i] == delete_list[j]):
                flag = 1
        if flag != 1:
            answer.append(arr[i])
    
    return answer