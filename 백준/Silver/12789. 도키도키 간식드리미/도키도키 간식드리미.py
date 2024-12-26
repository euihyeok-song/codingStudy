import sys

T = int(sys.stdin.readline())

stack = []
array = list(map(int, sys.stdin.readline().split(' ')))
curr = 1

while(True):
    
    # 양쪽 모두 번호가 있는 경우
    if stack and array:
        if array[0] != curr and stack[-1] != curr:
            stack.append(array[0])
            array.pop(0)    
        elif array[0] == curr:
            array.pop(0)
            curr += 1
        elif stack[-1] == curr:
            stack.pop()
            curr += 1
    elif not stack and array:
        if array[0] != curr:
            stack.append(array[0])
            array.pop(0)
        elif array[0] == curr:
            array.pop(0)
            curr += 1
    elif not array and stack:
        if stack[-1] == curr:
            stack.pop()
            curr += 1
        else:
            break
    elif not stack and not array:
        break


if not stack and not array:
    print("Nice")
else:
    print("Sad")