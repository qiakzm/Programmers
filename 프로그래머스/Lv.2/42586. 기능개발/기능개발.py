def solution(progresses, speeds):
    answer = []
    while progresses:
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
        
        count = 0
        
        while progresses and progresses[0] >= 100:
            del progresses[0], speeds[0]
            count += 1
        
        if count:
            answer.append(count)
                
    return answer
