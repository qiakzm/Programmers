def solution(citations):
    answer = 0
    # 논문 오름차순 정렬하기
    citations.sort()
    
    for i in range(len(citations)):
        # 발표한 논문 수 : n
        n = len(citations)
        # i보다 많이 인용된 논문 수 : 
        h = n - i
        # 정렬한 
        if citations[i] >= h:
            answer = h
            break
            
    return answer