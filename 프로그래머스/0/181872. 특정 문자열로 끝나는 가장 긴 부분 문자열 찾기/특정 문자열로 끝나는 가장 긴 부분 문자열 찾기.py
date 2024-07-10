def solution(myString, pat):
        
    answer = ''
    
    # find함수는 가장 먼저 나온 값의 index를 출력
    # rfind함수는 뒤에서 부터 값을 찾아줌
    start = myString.rfind(pat)
    
    if(len(pat) == 1):
        answer = myString[:start+1]
    else:
        end = start + len(pat)
        answer = myString[:end]

    return answer