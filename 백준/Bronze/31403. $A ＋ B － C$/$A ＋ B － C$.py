number = []

for _ in range(3):
    number.append(input())

for _ in range(1):
    print(int(number[0]) + int(number[1]) - int(number[2]))
    print(int(number[0] + number[1]) - int(number[2]))