def solution(people, limit):
    sort_people = sorted(people)
    cnt, i, j = 0, 0 ,len(sort_people)-1
    
    while(i <= j):
        
        if sort_people[i] + sort_people[j] <= limit:
            cnt += 1
            i += 1
            j -= 1
        else:
            cnt += 1
            j -= 1
        
    return cnt