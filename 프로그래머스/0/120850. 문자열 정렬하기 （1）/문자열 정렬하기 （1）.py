def solution(my_string):
    answer = []
    mstr = list(my_string)
    for i in mstr:
        if i.isdigit():
            answer.append(int(i))
            
    return sorted(answer)