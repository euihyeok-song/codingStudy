num = []

for _ in range(3):
    num.append(int(input()))
    
total = str(num[0] * num[1] * num[2])

for i in range(10):
    
    print(total.count(str(i)))
    