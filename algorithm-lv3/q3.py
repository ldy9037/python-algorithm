# 탐욕법 - 섬 연결하기
# 크루스칼 적용
def find_parent(parent_list, index):
    result = index

    if parent_list[index] == index: return result
    result = find_parent(parent_list, parent_list[index])
    
    return result

def solution(n, costs):
    answer = 0
    parent_list = list(range(n))

    costs.sort(key=lambda cost: cost[2])

    for cost in costs:
        source, destination, length = cost

        source_parent = find_parent(parent_list, source)
        destination_parent = find_parent(parent_list, destination)

        if source_parent == destination_parent: continue
        else: 
            answer += length
            if source_parent > destination_parent: parent_list[destination_parent] = source_parent
            else: parent_list[source_parent] = destination_parent

    return answer

n = 4
costs = [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]
print(solution(n, costs))
