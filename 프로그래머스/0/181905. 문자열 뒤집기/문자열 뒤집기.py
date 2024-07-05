def solution(my_string, s, e):
    
    answer = ''
    word =  reversed(list(my_string[s:e+1]))
    
    sentence = ''.join(word)
    
    answer = my_string[:s] + sentence + my_string[e+1:]
    
    return answer