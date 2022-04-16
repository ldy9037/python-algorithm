from datetime import datetime
from unittest import result

def korean_age(birth_year):
    return int(datetime.today().year) - birth_year + 1

year = int(input('생년 입력 : '))
age = korean_age(year)

print(age)