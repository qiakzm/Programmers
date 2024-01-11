def solution(s):
    answer = True
    cnt = 0
    
    for i in s:
        if i == '(':
            cnt += 1
        else:
            cnt -= 1
        if cnt == -1:
            return False
    
    if cnt == 0:
        if s[0] == ')':
            return False
        elif s[-1] == '(':
            return False
        return True

    if cnt != 0:
        return False

