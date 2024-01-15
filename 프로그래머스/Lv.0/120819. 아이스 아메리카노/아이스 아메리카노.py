def solution(money):
    answer = []
    drink = money // 5500
    exchange = int(money % 5500)
    answer.append(drink)
    answer.append(exchange)
    return answer