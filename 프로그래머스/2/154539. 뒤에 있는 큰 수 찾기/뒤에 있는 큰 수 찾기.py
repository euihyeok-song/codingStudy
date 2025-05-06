from collections import deque

def solution(numbers):
    stack, result = [], []
    
    for val in numbers[::-1]:
        
        while stack and stack[-1] <= val:
            stack.pop()
        
        if not stack:
            result.append(-1)
        else:
            result.append(stack[-1])
            
        stack.append(val)
        
    return result[::-1]