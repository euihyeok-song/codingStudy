import sys

while(True):
    
    m = int(sys.stdin.readline().rstrip())
    
    if m == 0:
        break
    
    # 투포인터의 시작과 끝점
    start = 0
    end = 0
            
    # 총 갯수
    cnt = 0
    
    # 범주 내에 문자의 개수를 저장
    dic = dict()
    
    sentence = list(sys.stdin.readline().rstrip())
    
    while(end < len(sentence)):
            
        if len(dic) < m:
            dic[sentence[end]] = dic.get(sentence[end], 0) + 1
            end += 1
        else:
            if sentence[end] in dic:
                dic[sentence[end]] += 1
                end += 1
            else:
                dic[sentence[start]] -= 1
                if dic[sentence[start]] == 0:
                    del dic[sentence[start]]
                start += 1

        if len(dic) <= m:
            cnt = max(cnt, end-start)
        
    print(cnt)