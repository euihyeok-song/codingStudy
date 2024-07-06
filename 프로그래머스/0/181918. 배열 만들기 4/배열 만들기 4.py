def solution(arr):
    i = 0
    stk = []
    
    while(i < len(arr)):
        
        if not stk:
            stk.append(arr[i])
            i += 1
        elif stk and stk[-1] < arr[i]:
                stk.append(arr[i])
                i += 1
        elif stk and stk[-1] >= arr[i]: 
                stk.pop()

    return stk