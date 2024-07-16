def solution(s):
    answer = ''
    
    if len(s) % 2 == 0:
        index = (len(s)//2) - 1
        answer = ''.join(s[index:index+2])
    else:
        answer = s[len(s)//2]
    
    return answer