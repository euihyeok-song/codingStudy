import sys
from itertools import combinations

input = sys.stdin.readline

N,K = map(int,input().rstrip().split(" "))
graph = [[] for _ in range(N)]

for idx in range(N):
    x, y = map(int, input().rstrip().split(" "))
    graph[idx] = (x,y)
    
case = combinations(graph,K)
min_distance = 200001

def calculate(house):
    
    total = 0
    
    for v_position in  graph:
        distance = []
        x, y = v_position[0], v_position[1]
        
        for h_position in house:
            a, b = h_position[0], h_position[1]
            
            distance.append(abs(x-a) + abs(y-b))
        
        short_path = min(distance)
        
        if total < short_path:
            total = short_path
                
    return total

for house in case:
    
    result = calculate(house)
    
    if result < min_distance:
        min_distance = result

print(min_distance)