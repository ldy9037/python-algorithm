# DFS/BFS - 네트워크
# DFS 사용
vertices = []

def search(vertex, computers):
    global vertices
    vertices[vertex] = True

    for i ,edge in enumerate(computers[vertex]):
        if not vertices[i] and edge:
            search(i, computers)


def solution(n, computers):
    answer = 0
    global vertices  
    vertices = [False] * n

    while not all(vertices):
        search(vertices.index(False), computers)
        answer += 1

    return answer

n = 3
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]

print(solution(n, computers))