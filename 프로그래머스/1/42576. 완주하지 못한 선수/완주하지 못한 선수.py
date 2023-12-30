def solution(participant, completion):
    hashd = {}
    sumhash = 0
    
    for part in participant:
        hashd[hash(part)] = part
        sumhash += hash(part)
        
    for com in completion:
        sumhash -= hash(com)
    
    return hashd[sumhash]