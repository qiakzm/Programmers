def solution(citations):
    # h-index = a번 이상 인용된 논문이 b편인 경우, a와 b 중 작은 값
    answer = 0
    citations.sort()  # 인용 횟수를 기준으로 정렬
    
    for i in range(len(citations)):
        h = len(citations) - i  # 현재 값 이상의 인용 횟수를 가진 논문의 수
        if citations[i] >= h:
            answer = h
            break

    return answer
