def solution(mats: list, park: list) -> int:
    mats.sort(reverse=True)
    
    for mat in mats:
        for i in range(len(park) - mat + 1):
            for k in range(len(park[i]) - mat + 1): 
                if park[i][k] == "-1" and can_spread_mat(park, i, k, mat):
                    return mat
                    
    return -1

def can_spread_mat(park: int, start_row: int, start_col: int, mat_size: int) -> bool:
    for i in range(start_row, start_row + mat_size):
        for k in range(start_col, start_col + mat_size):
            if park[i][k] != "-1": return False
            
    return True
            

mats = [3]
park = [["-1", "-1", "-1"],["-1", "-1", "-1"],["-1", "-1", "-1"]]

print(solution(mats, park))