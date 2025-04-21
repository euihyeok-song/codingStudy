def solution(s):
    
    num = list(map(int,s.split(" ")))
    
    return ''.join(str(min(num)) + " " + str(max(num))) 