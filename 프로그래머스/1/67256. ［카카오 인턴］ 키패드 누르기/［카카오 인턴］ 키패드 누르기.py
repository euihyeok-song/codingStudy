def solution(numbers, hand):
    answer = ''
    
    # 키패드 좌표 설정
    keypads = {
        1: (0, 0), 2: (0, 1), 3: (0, 2),
        4: (1, 0), 5: (1, 1), 6: (1, 2),
        7: (2, 0), 8: (2, 1), 9: (2, 2),
        '*': (3, 0), 0: (3, 1), '#': (3, 2)
    }
    
    # 초기 손 위치 설정
    left_pos = keypads['*']
    right_pos = keypads['#']
    
    # 왼손잡이 여부
    is_right_hand = hand == "right"
    
    for num in numbers:
        # 왼손으로 눌러야 하는 숫자
        if num in [1, 4, 7]:
            answer += 'L'
            left_pos = keypads[num]
        
        # 오른손으로 눌러야 하는 숫자
        elif num in [3, 6, 9]:
            answer += 'R'
            right_pos = keypads[num]
        
        # 가운데 숫자일 경우 거리 계산
        else:
            left_dist = abs(left_pos[0] - keypads[num][0]) + abs(left_pos[1] - keypads[num][1])
            right_dist = abs(right_pos[0] - keypads[num][0]) + abs(right_pos[1] - keypads[num][1])
            
            if left_dist < right_dist:
                answer += 'L'
                left_pos = keypads[num]
            elif right_dist < left_dist:
                answer += 'R'
                right_pos = keypads[num]
            else:
                if is_right_hand:
                    answer += 'R'
                    right_pos = keypads[num]
                else:
                    answer += 'L'
                    left_pos = keypads[num]
    
    return answer
