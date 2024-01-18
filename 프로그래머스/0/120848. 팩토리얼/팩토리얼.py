def pact(num):
    a = 1
    for i in range(1, num+1):
        a *= i
    return a

def solution(n):
    answer = 0
    if n == 0:
        answer = 0
    elif n == 1:
        answer = 1
    elif pact(2) <= n < pact(3):
        answer = 2
    elif pact(3) <= n < pact(4):
        answer = 3
    elif pact(4) <= n < pact(5):
        answer = 4
    elif pact(5) <= n < pact(6):
        answer = 5
    elif pact(6) <= n < pact(7):
        answer = 6
    elif pact(7) <= n < pact(8):
        answer = 7
    elif pact(8) <= n < pact(9):
        answer = 8
    elif pact(9) <= n < pact(10):
        answer = 9
    elif pact(10) == n:
        answer = 10
    return answer