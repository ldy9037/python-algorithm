def solution(wallet: list, bill: list) -> int:
    answer = 0
    
    wallet.sort()
    bill.sort()
    
    while not canPut(wallet, bill):
        bill[1] = fold(bill[1])
        bill.sort()
        answer += 1
    
    return answer

def canPut(wallet: list, bill: list) -> bool:
    return wallet[0] >= bill[0] and wallet[1] >= bill[1]     

def fold(length: int) -> list:
    return length // 2
    
wallet = [50, 50]
bill = [100, 241]
print(solution(wallet, bill))