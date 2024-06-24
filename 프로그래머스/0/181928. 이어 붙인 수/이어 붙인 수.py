def solution(num_list):
    answer = 0
    
    even = []
    odd = []
    
    for i in range(len(num_list)):
        if(num_list[i] % 2 != 0):
            odd.append(str(num_list[i]))
        else:
            even.append(str(num_list[i]))
            
    print(odd)
    print(even)
    A = ''.join(even)
    B = ''.join(odd)
    
    answer = int(A)+int(B)
            
    return answer