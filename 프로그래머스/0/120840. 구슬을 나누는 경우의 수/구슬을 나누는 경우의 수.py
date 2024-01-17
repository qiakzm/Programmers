def fact(num):
    a = 1
    for i in range(1, num + 1):
        a *= i
    return a

def solution(balls, share):
    answer = 0
    n = fact(balls)
    m = fact(share)
    nm = fact(balls - share)
    
    answer = n / (nm * m)
    return answer