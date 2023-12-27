def solution(my_strings, parts):
    answer = ''
    
    for s, e in enumerate(parts):
        answer += my_strings[s][e[0]:e[1]+1]
    return answer