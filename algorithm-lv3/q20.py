# 카카오 인턴십 - 불량 사용자
def check_include(b, u):
    result = False

    hide = b.count("*")
    
    if len(b) == len(u):
        same = 0
        for i in range(len(b)):
            if b[i] == u[i]: same += 1
        
        result = (same == len(b) - hide) 

    return result

def solution(user_id, banned_id):
    answer = []
    
    stack = [([], user_id, 0)]

    while stack:
        banned_list, user_list, banned_index = stack.pop()

        for u in user_list:
            if check_include(banned_id[banned_index], u): 
                b_temp = banned_list.copy()
                b_temp.append(u)

                u_temp = user_list.copy()
                u_temp.remove(u)

                if banned_index < len(banned_id) - 1: 
                    stack.append((b_temp, u_temp, banned_index + 1))
                else:
                    if len(b_temp) == len(banned_id):
                        answer.append(tuple(sorted(b_temp)))

    return len(set(answer))

user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id = ["fr*d*","******", "******"]

print(solution(user_id, banned_id))