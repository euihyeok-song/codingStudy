def solution(s):
    answer = True
#     pcount = 0
#     ycount = 0
    
#     for val in list(s):
#         if(val == 'p' or val == 'P'):
#             pcount += 1
#         elif(val == 'y' or val == 'Y'):
#             ycount += 1
    
#     if(pcount != ycount):
#         answer = False

#   모범답안
    if(s.lower().count('y') != s.lower().count('p')):
        answer = False
    
    return answer