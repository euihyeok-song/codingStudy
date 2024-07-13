def solution(picture, k):
    result = []
    answer = []
    
#     for val in picture:
#         word = ''
#         for idx in val:
#             word += idx * k
#         result.append(word)
        
#     for i in result:
#         for j in range(k):
#             answer.append(i)


    # 모범 답안 (replace 사용)
    for i in picture:
        for _ in range(k):
            answer.append(i.replace('.','.'*k).replace('x','x'*k))
    
        
    return answer