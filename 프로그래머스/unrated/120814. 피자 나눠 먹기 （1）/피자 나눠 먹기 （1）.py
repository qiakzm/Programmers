def solution(n):
    answer = 0
    tmp = n % 7
    
    if tmp == 0:
        answer = n // 7
    else:
        answer = n // 7 + 1
    return answer