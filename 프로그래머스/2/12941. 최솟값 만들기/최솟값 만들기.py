def solution(A,B):
    
    total = 0
    sort_A = sorted(A)
    sort_B = sorted(B,key=lambda x:-x)
    
    for idx in range(len(A)):
        total += sort_A[idx] * sort_B[idx]

    return total