# 카카오 블라인드 - 셔틀버스
def time_to_minute(time):
    hour, minute = time.split(":")    
    return (int(hour) * 60) + int(minute)

def minute_to_time(minute):
    s, r = divmod(minute, 60)
    return str(s).rjust(2, "0") + ":" + str(r).rjust(2,"0")

def solution(n, t, m, timetable):
    answer = []
    current_time = time_to_minute("09:00")
    
    timetable = sorted(list(filter(lambda time: time <= time_to_minute("18:00"), map(time_to_minute ,timetable))), reverse=True)

    for i in range(n): 
        passenger = []

        for k in range(m): 
            if timetable and timetable[-1] <= current_time:
                passenger.append(timetable.pop())

        if len(passenger) == m: answer.append(passenger[-1] - 1)
        else: answer.append(current_time)

        current_time += t
         
    return minute_to_time(max(answer))

n = 2
t = 10
m = 2
timetable =  ["09:10", "09:09", "08:00"]

print(solution(n, t, m, timetable))