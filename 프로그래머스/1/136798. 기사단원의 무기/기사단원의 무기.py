def solution(number, limit, power):

    answer = 0
    for i in range(1, number + 1):
        divisors = divide(i)
        if divisors > limit:
            answer += power
        else:
            answer += divisors
            
    return answer

def divide(n):
        count = 0
        for i in range(1, int(n ** 0.5) + 1):
            if n % i == 0:
                count += 1
                if i != n // i:
                    count += 1
        return count
