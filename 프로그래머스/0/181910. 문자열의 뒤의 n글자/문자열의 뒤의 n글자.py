def solution(my_string, n):
    string = list(my_string)
    
    start = len(string) - n
    print(start)
    count = 0
    
    while(count != start):
        del string[0]
        count += 1
    
    answer = ''.join(string)
    
    return answer


