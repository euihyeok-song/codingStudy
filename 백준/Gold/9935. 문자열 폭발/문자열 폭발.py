import sys

input = sys.stdin.readline

word = input().rstrip()
boom = input().rstrip()
boom_len = len(boom)

stack = []

for val in word:    
    stack.append(val)

    if stack[-1] == boom[-1] and len(stack) >= boom_len and stack[-1-boom_len+1:] == list(boom):
        for _ in range(boom_len):
            stack.pop()

if not stack:
    print("FRULA")
else:
    print(''.join(stack))

