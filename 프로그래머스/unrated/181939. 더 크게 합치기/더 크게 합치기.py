def solution(a, b):
    ab = int(str(a) + str(b))
    ba = int(str(b) + str(a))
    answer = 0
    
    if (ab > ba):
        answer = ab
    else:
        answer = ba
    return answer