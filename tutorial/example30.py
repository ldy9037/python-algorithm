def addZero(num):
    result = str(num)
    if num < 10:
        result = '0'+result
    
    return result

def printDate(date):    
    year, month, day = date
    print(str(year)+'/'+addZero(month)+'/'+addZero(day))

def addDay(date):
    year, month, day = date
    
    isLastMonth = (month, day) in [(1, 31), (2, 28), (3, 31), (4, 30), (5,
        31), (6, 30), (7, 31), (8, 31), (9, 30), (10, 31), (11, 30), (12, 31)]

    if isLastMonth:
        if month == 12: 
            year += 1
            month = 1
        else:
            month += 1
        day = 1 
    else:
        day += 1
    
    return year, month, day

date = tuple(map(int, input('년도, 월, 일 입력').split(' ')))

printDate(date)
printDate(addDay(date))