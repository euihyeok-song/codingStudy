def solution(my_string, queries):
    string = list(my_string)
    
    # for a,b in queries:
    #     string[a:b+1] = reversed(string[a:b+1])
    
    for a,b in queries:
        string[a:b+1] = string[a:b+1][::-1]
        
    answer = ''.join(string)
    return answer