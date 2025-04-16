def solution(n, words):
    
    use = []
    last = ""
    
    for idx,val in enumerate(words):
        
        if idx == 0:
            use.append(val)
            last = val[-1]
        elif val[0] == last and val not in use:
            use.append(val)
            last = val[-1]
        else:
            return [idx%n+1,idx//n+1]
    
    return [0,0]