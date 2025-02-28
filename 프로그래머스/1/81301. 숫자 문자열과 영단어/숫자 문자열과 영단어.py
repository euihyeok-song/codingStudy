def solution(s):
        
    dict = {"zero":0, "one":1, "two":2, "three":3, "four":4, "five":5, "six":6,
            "seven":7, "eight":8, "nine":9}
    
    word = ''
    num = ''
    
    for val in s:
        
        if val.isdigit():
            num += val
        else:
            word += val
        
        if word in dict.keys():
            num += str(dict[word])
            word = ''
            
    return int(num)