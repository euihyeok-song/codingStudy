num = list(map(int,input()))

digit = [0] * 10

for val in num:
    
    if val == 6 or val == 9:
        if digit[6] < digit[9]:
            digit[6] += 1
        else:
            digit[9] += 1
    else:
        digit[val] += 1
    
print(max(digit))
        