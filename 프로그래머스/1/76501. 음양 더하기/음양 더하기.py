def solution(absolutes, signs):
    
    for idx,val in enumerate(signs):
        if val == False:
            absolutes[idx] = -absolutes[idx]
    
    return sum(absolutes)