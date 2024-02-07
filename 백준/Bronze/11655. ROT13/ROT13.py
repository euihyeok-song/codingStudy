# ROT13

sentence = list(input())

ans = []

for val in sentence:

    number = 0
    
    if(val.islower()):
        number = ord(val) + 13
        if(number > ord('z')):
            number -= 26
        ans.append(chr(number))
    elif(val.isupper()):
        number = ord(val) + 13
        if(number > ord('Z')):
            number -= 26
        ans.append(chr(number))
    elif(val.isspace()):
        ans.append(' ')
    else:
        ans.append(val)

for i in range(len(ans)):
    if(i < len(ans)-1):
        print(ans[i], end='')
    else:
        print(ans[i])