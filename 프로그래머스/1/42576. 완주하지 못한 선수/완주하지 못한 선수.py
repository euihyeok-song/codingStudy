from collections import Counter

def solution(participant, completion):

    p_count = Counter(participant)
    c_count = Counter(completion)

    for name in p_count:
        if p_count[name] != c_count[name]:
            return name
