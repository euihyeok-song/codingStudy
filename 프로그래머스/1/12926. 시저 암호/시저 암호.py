def solution(s, n):
    answer = ''
    for char in s:
        if char == ' ':
            answer += ' '
        elif char.islower():
            answer += chr((ord(char) - ord('a') + n) % 26 + ord('a'))
        elif char.isupper():
            answer += chr((ord(char) - ord('A') + n) % 26 + ord('A'))
    return answer
