def solution(arr):
    answer = 0
    tmp = 0
    for i in arr:
        tmp += i
        answer = tmp / len(arr)
    return answer