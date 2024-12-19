def solution(a, b, c, d):
    
    num = [a,b,c,d]
    sets = list(set(num))
    
    if len(sets) == 1:
        return 1111 * a
    elif len(sets) == 2:
        if(num.count(a) == 1):
            return (10 * b + a)**2
        elif(num.count(a) == 2):
            return (sets[0]+sets[1]) * (sets[1]-sets[0])
        if(num.count(a) == 3):
            result = list(set(num) - {a})
            return (10 * a + result[0])**2
            
    elif len(sets) == 3:
        for j in num:
            if num.count(j) == 2:
                newNum = [ x for x in num if x != j]
                return newNum[0] * newNum[1]
    else:
        return min(a,b,c,d)
    
    