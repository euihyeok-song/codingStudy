def solution(s):
    stack = []
    
    for val in s:
        if not stack:
            stack.append(val)
        else:
            if stack[-1] == val:
                stack.pop()
            else:
                stack.append(val)

    return int(not stack)