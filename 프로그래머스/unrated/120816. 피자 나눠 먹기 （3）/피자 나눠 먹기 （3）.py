def solution(slice, n):
    answer = 0
    tmp = n % slice
    
    if tmp == 0:
        answer = n / slice
    elif tmp != 0:
        answer = n // slice + 1
    return answer