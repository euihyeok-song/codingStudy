from collections import Counter
import re

def solution(s):
    
    # 결국 가장 많이 나오는 순서대로 넣어주면 OK
    cnt = Counter(list(re.sub("{|}","",s).split(',')))
    result = []
    
    for x,_ in cnt.most_common():
        result.append(int(x))
    
    
    return result

