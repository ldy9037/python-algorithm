# 2018 카카오 블라인드 - 추석트래픽
from datetime import datetime

def convert_timestamp(line):
    end_date, end_time, duration = line.split()
    end_timestamp = datetime.strptime(end_date + " " + end_time, '%Y-%m-%d %H:%M:%S.%f').timestamp() * 1000

    return end_timestamp - (float(duration.replace("s","")) * 1000) + 1,end_timestamp

def solution(lines):
    answer = [1] * len(lines)

    times = []
    for line in lines: times.append(convert_timestamp(line))
    
    for i in range(len(times)):
        for k in range(i + 1, len(times)):
            std = times[i][1]
            
            start_ts, end_ts = times[k]
            if start_ts < std + 1000: answer[i] += 1
        
    return max(answer)

lines = ["2016-09-15 01:00:04.001 2.0s", "2016-09-15 01:00:07.000 2s"]

#7

print(solution(lines))