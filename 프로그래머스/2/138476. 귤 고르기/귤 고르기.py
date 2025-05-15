from collections import Counter

def solution(k, tangerine):
    count = Counter(tangerine)
    sizes = sorted(count.values(), reverse=True)
    
    total = 0
    answer = 0
    for size in sizes:
        total += size
        answer += 1
        if total >= k:
            break
            
    return answer
