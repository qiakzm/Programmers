def solution(arr, n):
    
    for k, i in enumerate(arr):
        if len(arr) % 2 == 1:
            if k % 2 == 0:
                arr[k] += n
        else:
            if k % 2 == 1:
                arr[k] += n
    return arr