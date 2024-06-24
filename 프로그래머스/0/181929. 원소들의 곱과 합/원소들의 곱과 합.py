def solution(num_list):
    answer = 0
    
    product = 1
    square = 0
    
    for i in range(len(num_list)):
        product *= num_list[i]
        square += num_list[i]
    
    tot_square = square * square
    
    if(product > tot_square):
        answer = 0
    else:
        answer = 1
    
    return answer