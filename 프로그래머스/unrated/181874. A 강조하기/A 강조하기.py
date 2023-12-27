def solution(myString):
    answer = ''
    
    myString = myString.lower()
    
    for i in range(len(myString)):
        if myString[i] == 'a':
            answer += myString[i].upper()
        elif myString[i].isupper() != 'A':
            answer += myString[i].lower()
            
    return answer