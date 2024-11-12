def solution(num, k):
    answer = 0
    k = str(k)
    for i in str(num):
        if k == i:
            answer = (str(num).index(i))+1
        elif k != i:
            pass
    return answer if answer != 0 else -1