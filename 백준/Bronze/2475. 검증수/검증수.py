number = list(map(int, input().split(' ')))

print((number[0]*number[0] + number[1]*number[1] + number[2]*number[2] + number[3]*number[3] + number[4]*number[4])%10)