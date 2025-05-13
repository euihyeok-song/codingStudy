def solution(arr1, arr2):
    result = []
    
    for i in range(len(arr1)):
        row_result = []
        for j in range(len(arr2[0])):
            cell = 0
            for k in range(len(arr2)):
                cell += arr1[i][k] * arr2[k][j]
            row_result.append(cell)
        result.append(row_result)
        
    return result
