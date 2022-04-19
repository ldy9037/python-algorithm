num = int(input('반복 수 : '))
prev_row = "0000000000000000000000000000000000000001000000000000000000000000000000000000000"
print(prev_row)
pattern = {"111" : "0", "110": "1", "101": "0", "100": "1", "011": "1", "010": "0", "001": "1", "000": "0"}

for i in range(num):
    now_row = prev_row[1]
    k = 0

    while k + 2 <= len(prev_row) -1: 
        now_row += pattern[prev_row[k:k+3]]
        k += 1
    else:
        now_row += prev_row[k]
        print(now_row)
     
    prev_row = now_row
        
    
        
