def solution(a, b):
    answer = 0
    
    ab = int(str(a) + str(b))
    ab2 = 2*a*b
    
    if (ab > ab2):
        answer = ab
    else:
        answer = ab2
    return answer