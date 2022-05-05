# DFS/BFS - 여행경로
# DFS로 풀어보았는데 성능 면에서 아쉬움. 개선해봐야겠음
def solution(tickets):
    answer = []
    stack = [([],tickets,"ICN")]
    
    while stack:
        history, remaining_tickets, current = stack.pop()

        if len(history) == len(tickets): 
            history.append(current)
            answer.append(history)
            continue

        for ticket in remaining_tickets:
            if ticket[0] == current: 
                remaining_tickets_temp = remaining_tickets.copy()
                remaining_tickets_temp.remove(ticket)
                stack.append((history + [ticket[0]], remaining_tickets_temp, ticket[1]))

    answer.sort()

    return answer[0] 

tickets = [["ICN", "SFO"], ["SFO", "ATL"], ["ATL", "ICN"], ["ICN", "SFO"]]
print(solution(tickets))

#["ICN", "AOO", "BOO", "COO", "DOO", "EOO", "DOO", "COO", "BOO", "AOO"]