def solution(S, C):
    answer = 0

    stack = []
    
    for char, price in zip(S,C):
        if not stack: stack.append((char, price))
        else: 
            p_char, p_price = stack[-1]
            
            if p_char == char:
                if p_price < price:
                    stack.pop()
                    answer += p_price
                    stack.append((char, price))
            else: stack.append((char, price)) 

    print(stack)
    return answer

S = "aabbcc"
C = [1,2,1,2,1,2]

print(solution(S, C))