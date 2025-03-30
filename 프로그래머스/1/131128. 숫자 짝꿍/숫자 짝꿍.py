def solution(X, Y):
    count_X = [0] * 10
    count_Y = [0] * 10

    for digit in X:
        count_X[int(digit)] += 1
    for digit in Y:
        count_Y[int(digit)] += 1

    result = []
    for i in range(9, -1, -1):
        result.extend([str(i)] * min(count_X[i], count_Y[i]))

    if not result:
        return "-1"
    if result[0] == "0":
        return "0"
    
    return "".join(result)
