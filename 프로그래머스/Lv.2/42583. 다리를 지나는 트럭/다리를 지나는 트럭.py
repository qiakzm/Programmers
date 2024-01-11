def solution(bridge_length, weight, truck_weights):
    answer = 0
    going = []  # 다리 위에 있는 트럭들
    going_times = []  # 각 트럭이 다리를 건너는 데 걸린 시간
    
    # 1. 대기중인 트럭이 있거나 건너고 있는 트럭이 있는 경우
    #    = 트럭이 다 건널 때 까지
    while truck_weights or going:
        answer += 1

        # 다리를 다 건넌 트럭은 리스트에서 제거
        if going_times and going_times[0] == bridge_length:
            going.pop(0)
            going_times.pop(0)
            
        # 다음 트럭이 다리에 올라갈 수 있는지 확인
        if truck_weights and sum(going) + truck_weights[0] <= weight:
            going.append(truck_weights.pop(0))
            going_times.append(0)
            
        # 다리 위의 트럭들의 건너는 시간을 갱신
        for i in range(len(going_times)):
            going_times[i] += 1

    return answer
