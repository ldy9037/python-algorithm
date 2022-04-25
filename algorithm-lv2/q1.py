# 해시 - 전화번호 목록
# 성능 개선 필요함. 
"""
문자열 길이 순으로 정렬해서 비교하고 있는데 그냥 문자열 순으로 정렬해서 인접한 것들끼리만 비교 할 수도 있겠음. 
그런데 해시를 사용한다는 조건이 있기 때문에 그대로 두겠음.
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
해시를 생각하지 않는다면 아래와 같이 풀 수 있음. 
정렬 후 인접한 것들끼리 비교. 
그냥 sort하면 문자열 순으로 정렬됨.

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
"""


phone_book = ["119","97674223","1195524421"]
print(solution(phone_book))