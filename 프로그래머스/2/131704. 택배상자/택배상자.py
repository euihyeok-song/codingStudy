def solution(order):
    stack = []
    current = 1
    index = 0
    while current <= len(order):
        if order[index] == current:
            index += 1
            current += 1
        elif stack and stack[-1] == order[index]:
            stack.pop()
            index += 1
        else:
            stack.append(current)
            current += 1
    while stack and stack[-1] == order[index]:
        stack.pop()
        index += 1
        
    return index
