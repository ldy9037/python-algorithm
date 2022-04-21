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