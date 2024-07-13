str = input()

answer = list(str)
result = []

for val in answer:
    if( val.isupper() ):
        result.append(val.lower())
    else:
        result.append(val.upper())
        
str = ''.join(result)
print(str)
