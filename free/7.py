def solution(edges: list) -> list:
    answer = [0, 0, 0, 0]

    sources = dict()
    dests = dict()
    nodes = set()
    
    for edge in edges:
        nodes.add(edge[0])
        nodes.add(edge[1])
    
    for node in nodes:
        sources[node] = []
        dests[node] = []

    for i in range(len(edges)):
        sources[edges[i][0]].append(edges[i][1])
        dests[edges[i][1]].append(edges[i][0])

    for i in sources.keys():
        if len(sources[i]) >= 2 and len(dests[i]) == 0:
            answer[0] = i
            break
        
    for i in sources.keys():
        if answer[0] in dests[i]:
            dests[i].remove(answer[0])
        
        if (len(sources[i]) == 1 or len(sources[i]) == 0) and len(dests[i]) == 0:
            answer[2] += 1
        
        if len(sources[i]) == 2 and len(dests[i]) == 2:
            answer[3] += 1
            
    answer[1] = len(sources[answer[0]]) - answer[2] - answer[3]
    
    return answer

#edges = [[4, 11], [1, 12], [8, 3], [12, 7], [4, 2], [7, 11], [4, 8], [9, 6], [10, 11], [6, 10], [3, 5], [11, 1], [5, 3], [11, 9], [3, 8]]
edges = [[2, 1], [2, 3],[1,1], [3,3]]
print(solution(edges))
