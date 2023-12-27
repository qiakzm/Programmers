def solution(num_list):
    answer = 0
    
    a = sum(num_list[i] for i in range(1, len(num_list), 2))
    b = sum(num_list[i] for i in range(0, len(num_list), 2))
    
    if a > b:
        answer = a
    else:
        answer = b
    return answer