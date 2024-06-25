def solution(date1, date2):
    answer = 0
    
    compare1 = list(date1)
    compare2 = list(date2)
    
    for i in range(3):
        if(compare1[i] > compare2[i]):
            break
        elif(compare1[i] == compare2[i]):
            continue
        else:
            answer = 1
            break
    
    return answer