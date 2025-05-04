import re
from collections import Counter

def solution(str1, str2):
    
    left, right = [], []
    
    for idx1 in range(len(str1)-1):
        if str1[idx1].isalpha() and str1[idx1+1].isalpha():
            left.append(str1[idx1].lower()+str1[idx1+1].lower())
    
    for idx2 in range(len(str2)-1):
        if str2[idx2].isalpha() and str2[idx2+1].isalpha():
            right.append(str2[idx2].lower()+str2[idx2+1].lower())

    left_Counter = Counter(left)
    right_Counter = Counter(right)
            
    # 교집합
    intersection = sum((left_Counter & right_Counter).values())
    
    # 합집합
    union = sum((left_Counter | right_Counter).values())
    
    return int((intersection/union) * 65536) if union != 0 else 65536