import heapq

def solution(operations):
    answer = []
    
    for command in operations:
        if command[0] == 'I':
            heapq.heappush(answer, int(command[2:]))
        elif command[0] == 'D':
            if command[2] == '-':
                if answer:
                    answer.remove(min(answer))
            elif command[2] == '1':
                if answer:
                    answer.remove(max(answer))

    return [max(answer), heapq.heappop(answer)] if answer else [0, 0]