def solution(babbling):
    oong = ["aya", "ye", "woo", "ma"]
    for k, i in enumerate(babbling):
        for j in oong:
            if j * 2 in i:
                break
            babbling[k] = babbling[k].replace(j, " ")
        babbling[k] = babbling[k].replace(" ", "")
    return babbling.count("")