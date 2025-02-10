import sys

input = sys.stdin.readline

while True:
    
    maxArea = 0
    stack = []
    height = list(map(int,input().rstrip().split(' ')))
    
    n = height[0]
    
    if n == 0:
        break
    
    height = height[1:]
    
    for i in range(n):
        start = i  

        while stack and stack[-1][0] > height[i]:
            h, idx = stack.pop()
            maxArea = max(maxArea, h * (i - idx))
            start = idx  

        stack.append((height[i], start))  

    for h, idx in stack:
        maxArea = max(maxArea, h * (n - idx))

    print(maxArea)   
