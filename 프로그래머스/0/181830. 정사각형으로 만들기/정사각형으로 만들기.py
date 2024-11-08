def solution(arr):
    answer = []
    temp = len(arr) - len(arr[0])
    if temp > 0:
        for i in arr:
            answer.append(i + [0] * temp)
    elif temp < 0:
        for _ in range(abs(temp)):
            arr.append([0] * len(arr[0]))
        answer = arr
    else:
        answer = arr       
    return answer