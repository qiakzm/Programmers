def solution(array):
    answer = 0
    tmp = sorted(array)
    answer = tmp[len(tmp)//2]
    return answer