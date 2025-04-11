import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    
    first = list(input().rstrip().split(" "))
    second = list(input().rstrip().split(" "))
    first_tree = [[] for _ in range(len(first))]
    second_tree = [[] for _ in range(len(second))]
    
    # 현재를 가르키고 있는 커서 (first)
    curr = 0
    for val in first:
        if val != "#":
            first_tree[curr].append(1)
            curr += 1
        else:
            curr -= 1
            
        
    # 현재를 가르키고 있는 커서 (second)
    curr = 0
    for val in second:
        if val != "#":
            second_tree[curr].append(1)
            curr += 1
        else:
            curr -= 1
    
    if first_tree == second_tree:
        print("The two trees are isomorphic.")
    else:
        print("The two trees are not isomorphic.")