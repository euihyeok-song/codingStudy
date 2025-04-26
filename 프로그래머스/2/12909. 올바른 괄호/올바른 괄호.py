def solution(s):
    
    stack = []
    
    for val in list(s):
        if not stack or val == "(":
            stack.append(val)
        else:
            stack.pop()

    return stack == []