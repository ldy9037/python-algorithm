# 정렬 - k번째수
def solution(array, commands):
    answer = []

    for start, end, index in commands:
        answer.append(sorted(array[start -1:end])[index -1])

    return answer

array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

solution(array, commands)