from collections import deque

def solution(cacheSize, cities):
    
    dq = []
    time = 0
    
    if cacheSize == 0:
        return 5 * len(cities)
    
    for city in cities:
        city = city.lower()
        if len(dq) < cacheSize:
            if city not in dq:
                dq.append(city)
                time += 5
            else:
                dq.pop(dq.index(city))
                time += 1
                dq.append(city)
        else:
            if city not in dq:
                dq.pop(0)
                dq.append(city)
                time += 5
            else:
                dq.pop(dq.index(city))
                time += 1
                dq.append(city)
    
    return time