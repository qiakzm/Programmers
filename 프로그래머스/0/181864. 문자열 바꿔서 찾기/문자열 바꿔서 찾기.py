def solution(myString, pat):
    k = ''
    for i in range(0, len(myString)):
        if myString[i] == 'A':
            k += 'B'
        elif myString[i] == 'B':
            k += 'A'
    
    return 1 if k.find(pat) != -1 else 0
