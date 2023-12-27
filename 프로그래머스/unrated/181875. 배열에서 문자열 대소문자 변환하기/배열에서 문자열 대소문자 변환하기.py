def solution(strArr):
    answer = []
    
    for i in range(len(strArr)):
        if i % 2 == 0:
            answer += [strArr[i].lower()]
        else:
            answer += [strArr[i].upper()]
    return answer