# 해시 - 전화번호 목록
# 성능 개선 필요함. 
"""
def solution(phone_book):
    phone_book.sort(key=len)
    phone_set = set()
    phone_len = set()

    for phone in phone_book:
        for length in phone_len: 
            if phone[:length] in phone_set: return False
                    
        phone_len.add(len(phone))
        phone_set.add(phone)

    return True
"""
def solution(phoneBook):
    #phoneBook = sorted(phoneBook)
    phoneBook.sort()
    print("정렬",phoneBook)

    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        print('첫 번째', p1)
        print('두 번째', p2)
        if p2.startswith(p1):
            return False
    return True


phone_book = ["119","97674223","1195524421"]
print(solution(phone_book))