# 카카오 인턴쉽 - 거리두기 확인

def check(place):
    for i in range(len(place)):
        for k in range(len(place[i])):
            if place[i][k] == "P":
                stack = [(i, k, 0)]

                while stack:
                    row, col, depth = stack.pop()

                    if place[row][col] == "X": continue
                    if depth >= 1 and row == i and col == k: continue
                    
                    if depth >= 1 and place[row][col] == "P": 
                        return 0

                    if depth <= 1:
                        if row - 1 >= 0: stack.append((row - 1, col, depth + 1))
                        if col - 1 >= 0: stack.append((row, col - 1, depth + 1))
                        if row + 1 <= 4: stack.append((row + 1, col, depth + 1))
                        if col + 1 <= 4: stack.append((row, col + 1, depth + 1))
    return 1

def solution(places):
    answer = []

    for place in places:
        answer.append(check(place))

    return answer

places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
print(solution(places))