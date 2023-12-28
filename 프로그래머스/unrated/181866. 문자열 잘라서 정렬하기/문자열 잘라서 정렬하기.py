def solution(myString):
    answer = []
    a = sorted(myString.split("x"))
    for i in a:
        if i != "":
            answer.append(i)
    return answer