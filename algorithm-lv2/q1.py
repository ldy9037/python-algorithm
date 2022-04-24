# 코딩테스트 연습 - 전화번호 목록
def solution(phone_book):
    phone_book.sort(key=len)
    phone_set = set()

    for phone in phone_book:
        for prev_phone in phone_set: 
            if phone.startswith(prev_phone): return False
        
        phone_set.add(phone)

    return True

phone_book = ["119","1195524421", "97674223"]
print(solution(phone_book))