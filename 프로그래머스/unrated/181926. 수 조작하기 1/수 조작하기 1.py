def solution(n, control):
    
    wasd = {
        'w' : 1,
        's' : -1,
        'd' : 10,
        'a' : -10
    }
    
    for i in control:
        n += wasd[i]
    return n