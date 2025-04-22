from collections import deque
import math

def solution(progresses, speeds):
    
    dq_pro = deque(progresses)
    dq_spd = deque(speeds)
    num, cnt, answer  = 0, 0, []
    
    while dq_pro:
        if dq_pro[0] + num * dq_spd[0] >= 100:
            dq_pro.popleft()
            dq_spd.popleft()
            cnt += 1
        else:
            if cnt > 0:
                answer.append(cnt)
                cnt = 0
            else:
                num += 1
        
        # 마지막 요소 처리
        if not dq_pro:
            answer.append(cnt)
            
    return answer