def solution(arr):
    answer = [arr[0]]
    
    for i in range(0, len(arr)):
        if arr[i] != answer[-1]:
            answer.append(arr[i])
    
    return answer