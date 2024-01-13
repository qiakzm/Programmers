def solution(phone_book):
    #1. phone_book 요소 해쉬 1로 지정
    hash_map = {}
    for number in phone_book:
        hash_map[number] = 1
    
    #2. 접두어가 해시맵에 존재하는가
    for phone_number in phone_book:
        jubdoo = ''
        for number in phone_number:
            jubdoo += number
            #3. 접두어 찾기.(본인 제외)
            if jubdoo in hash_map and jubdoo != phone_number:
                return False
    return True