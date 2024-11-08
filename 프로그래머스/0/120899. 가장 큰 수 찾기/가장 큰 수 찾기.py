def solution(array):
    answer = []
    max_a = max(array)
    answer.append(max_a)
    for i in range(len(array)):
        if array[i] == max_a:
            answer.append(i)
    return answer