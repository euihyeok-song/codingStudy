from collections import deque

def solution(priorities, location):
    
    cnt = 0
    dq = deque((x,y) for x,y in enumerate(priorities))
        
    while dq:
        
        max_pro = max(dq, key=lambda x: x[1])[1]
        
        if dq[0][1] == max_pro and dq[0][0] == location:
            break
        elif dq[0][1] == max_pro and dq[0][0] != location:
            dq.popleft()
            cnt += 1
        else:
            dq.append(dq.popleft())
            
    return cnt+1