from collections import Counter

def solution(topping):
    
    left, right = set(), Counter(topping)
    cnt = 0
    
    for val in topping:
        left.add(val)
        right[val] -= 1
        if right[val] == 0:
            del right[val]
        if len(left) == len(right):
            cnt += 1
    
    return cnt