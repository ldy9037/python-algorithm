# 카카오 - 크레인 인형뽑기 게임

def solution(board, moves):
    answer = 0
    doll_stack = []

    for move in moves: 
        selected = 0
        
        for depth in range(len(board)): 
            selected = board[depth][move - 1]
        
            if not selected == 0:
                board[depth][move - 1] = 0

                if  len(doll_stack) > 0 and doll_stack[-1] == selected: 
                    doll_stack.pop()
                    answer += 2
                else:
                    doll_stack.append(selected)
                break
        
    return answer

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]

print(solution(board, moves))

"""
행과 열을 바꾼 후 0을 제거해서 처리하려다가 코드가 너무 지저분해져서 위 처럼 했었음. 그런데 다른 사람의 풀이를 보니 딱 원하던 모양새의 풀이가 있어서 적어둠. 

def solution(board, moves):
    cols = list(map(lambda x: list( filter(lambda y: y > 0, x) ), zip(*board)))

    print(cols)
    a, s = 0, [0]

    for m in moves:
        if len(cols[m - 1]) > 0:
            if (d := cols[m - 1].pop(0)) == (l := s.pop()):
                a += 2
            else:
                s.extend([l, d])

    return a
"""