# 탐욕법 - 단속카메라
# 이게 왜 lv3..? 
def solution(routes):
    highway = []

    routes.sort(key=lambda route: route[1])
    
    for route in routes:
        if highway and highway[-1][1] >= route[0]: continue
        else: 
            highway.append(route)

    return len(highway)

routes = [[-20,-15], [-14,-5], [-18,-13], [-5,-3]]
print(solution(routes))