def solution(participant, completion):
    #1. 헤시 딕셔너리, 해시 합 만들기
    hashdict = {}
    sumhash = 0
    
    #2. 참가자 해시값 합 구하기
    for part in participant:
        hashdict[hash(part)] = part
        sumhash += hash(part)
        
    #3. 완주자 해시값 빼기
    for comp in completion:
        sumhash -= hash(comp)
        
    
        
    #4. 남은 해시값의 주인이 답
    return hashdict[sumhash]