def solution(hp):
    #장군: 5, 병정: 3, 일: 1
    J = hp // 5
    B = (hp % 5) // 3
    I = (hp % 5) % 3
    answer = J + B + I
    return answer