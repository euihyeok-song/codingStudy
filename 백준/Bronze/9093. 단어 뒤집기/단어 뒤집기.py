#단어뒤집기 9093번

import sys

# 입력받을 개수 times로 받기
times = int(sys.stdin.readline())

for i in range(times):
    
    # slicing_store = []
    function_store = []
    # 2차원 배열을 선언해서, 입력받는 문장을 단어 단위로 잘라서 알파벳 단위로 저장
    sentence = sys.stdin.readline().split()
    
    for token in sentence:
        word = list(map(str,token))
        # 1. 리스트 슬라이싱 사용
        # new_token = word[::-1]
        # new_word = "".join(new_token)
        # slicing_store.append(new_word)
        
        # 2. reverse함수 사용 -> reverse함수는 return값 없음 
        word.reverse()     
        new_word = "".join(word)
        function_store.append(new_word)
        

    # print(" ".join(slicing_store))
    print(" ".join(function_store))