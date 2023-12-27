def solution(num_list):
    answer = 0
    mul = 1
    add = 0
    
    for i in num_list:
        mul *= i
        add += i
        
    if (mul > add * add):
        answer = 0
    else:
        answer = 1

    return answer