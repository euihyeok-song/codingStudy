# 1. 필수적으로 + 와 =을 위해서 4개는 소요된다

# 각 숫자를 구성하는 총 성냥개비 갯수
# 들어갈 수 있는 최소 갯수: 4(11) 최대 갯수: 14(88)
num = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]

# + 와 = 을 제외한 총 성냥개비 갯수
N = int(input()) - 4

# 한자리씩 넣어보기
for i in range(10):
    for j in range(10):
        for k in range(10):
            for l in range(10):
                for m in range(10):
                    for n in range(10):
                        if (num[i] + num[j] + num[k] + num[l] + num[m] + num[n] == N) and (10*i + j + 10*k + l == 10*m + n):
                            print(str(i)+str(j)+'+'+str(k)+str(l)+"="+str(m)+str(n))
                            exit()
                            
print("impossible")

