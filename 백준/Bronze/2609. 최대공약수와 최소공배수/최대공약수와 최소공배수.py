import math

number = list(input().split(' '))

A = int(number[0])
B = int(number[1])

print(math.gcd(A,B))
print(math.lcm(A,B))