def solution(myString, pat):
    answer = 0
    str1 = list(myString)
    str2 = list(pat)
    
    for i in range(len(str1)):
        if(str1[i] == str2[0] and str1[i:i+len(str2)] == str2[:]):
            answer += 1
    
    return answer