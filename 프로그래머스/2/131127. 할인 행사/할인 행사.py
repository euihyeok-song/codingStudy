from collections import Counter

def solution(want, number, discount):
    
    want_dict = dict()
    for idx in range(len(want)):
        want_dict[want[idx]] = number[idx]
    
    st,cnt = 0,0
    while(st < len(discount)):
        
        if want_dict == dict(Counter(discount[st:st+10])):
            cnt += 1
            
        st += 1
    
    return cnt