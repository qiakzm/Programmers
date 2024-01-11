def solution(priorities, location):
    answer = 0
    
    while priorities:
        front = priorities.pop(0)
        if any(front < p for p in priorities):
            priorities.append(front)
        else:
            answer += 1
            if location == 0:
                break
        location = (location - 1 + len(priorities)) % len(priorities)
    
    return answer
