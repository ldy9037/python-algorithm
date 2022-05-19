# 2020 카카오 블라인드 - 문자열 압축

def solution(s):
    answer = [0] * ((len(s)  // 2) + 1)

    for i in range((len(s)  // 2) + 1):
        slice_length = i + 1
        k = 0
        stack = []

        while k <= len(s): 
            current = s[k:k + slice_length]
            k += slice_length
            
            count = 1
            if stack:
                prev, prev_count = stack.pop()
                
                if prev == current: count = prev_count + 1
                else: stack.append((prev, prev_count))
            stack.append((current, count))

        for string, count in stack:
            answer[i] += len(str(string))
            if count > 1: answer[i] += len(str(count))

    return min(answer)

s = ""
#7
print(solution(s))