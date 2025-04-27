def solution(s):

    cnt = 0
    zero_cnt = 0
    
    while(s != "1"):
        rm_zero = ""
        for val in list(s):
            if val != "0":
                rm_zero += val
            else:
                zero_cnt += 1
        
        s = str(bin(len(rm_zero)))[2:]
        cnt += 1
    
    return cnt,zero_cnt