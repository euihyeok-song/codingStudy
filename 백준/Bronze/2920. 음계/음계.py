num = list(map(int,input().split()))
asc = sorted(num)
desc = sorted(num, reverse=True)

if(num== asc):
    print("ascending")
elif(num == desc):
    print("descending")
else:
    print("mixed")

