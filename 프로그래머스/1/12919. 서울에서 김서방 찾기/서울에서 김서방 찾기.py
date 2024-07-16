def solution(seoul):
    answer = ''
#     index = 0
    
#     print(index('Kim'))
    
#     for idx,val in enumerate(seoul):
#         if val == 'Kim':
#             index = idx
    
#     answer = "김서방은 " + str(index) + "에 있다"
    
    # 모법답안
    
    answer = "김서방은 " + str(seoul.index('Kim')) + "에 있다"
    
    return answer