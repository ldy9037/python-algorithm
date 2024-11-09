def solution(video_len: str, pos: str, op_start: str, op_end: str, commands: str) -> str:
    answer = minute_to_second(pos)
    video_len_sec = minute_to_second(video_len)
    op_start_sec = minute_to_second(op_start)
    op_end_sec = minute_to_second(op_end)
    
    answer = jump_to_ops(answer, op_start_sec, op_end_sec)
    
    for command in commands:
        if command == "next":
            answer = answer + 10 if answer + 10 < video_len_sec else video_len_sec
        else:
            answer = answer - 10 if answer - 10 > 0 else 0
        
        answer = jump_to_ops(answer, op_start_sec, op_end_sec)
    
    return second_to_minute(answer)
    
def minute_to_second(time: str) -> int:
    minute, second = map(int,time.split(":"))

    return minute * 60 + second

def second_to_minute(time: int) -> str:
    minute, second = divmod(time, 60)

    return f"{minute:02d}:{second:02d}"

def jump_to_ops(now: int, op_start_sec: int, op_end_sec: int) -> int:
    return op_end_sec if now >= op_start_sec and now <= op_end_sec else now
        

print(solution("10:55", "00:05", "00:15", "06:55", ["prev", "next", "next"]))
# 06:55
    