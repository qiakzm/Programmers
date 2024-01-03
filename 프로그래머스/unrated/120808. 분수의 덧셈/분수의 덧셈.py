def solution(numer1, denom1, numer2, denom2):
    answer = []
    num = numer1*denom2 + numer2*denom1
    deno = denom1*denom2
    
    gcd = 0
    for i in range(min(num,deno), 0, -1):
        if num % i == 0 and deno % i == 0:
            gcd = i
            break
    answer = [num//gcd, deno//gcd]
    return answer