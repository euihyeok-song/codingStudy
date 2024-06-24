def solution(my_string, index_list):
    
    string = list(my_string)
    new = []
    
    for i in range(len(index_list)):
        new.append(string[index_list[i]])
    
    answer = ''.join(new)
    return answer