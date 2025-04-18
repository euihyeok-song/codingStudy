from collections import deque

def solution(s):
    
    dq = deque(list(s))
    cnt = 0
    
    for _ in range(len(s)):
        dq.append(dq.popleft())
        st = "".join(dq)
        
        prev = ""
        while prev != st:
            prev = st
            st = st.replace("()", "").replace("{}", "").replace("[]", "")
            
        if st == "":
            cnt += 1
        
    return cnt