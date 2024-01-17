def solution(num_list):
    answer = 0
    for i in num_list:
        while i != 1:
            if i % 2 == 0:
                answer += 1
                i = int(i/2)
            elif i % 2 == 1:
                answer += 1
                i = int((i-1)/2)
    return answer