def getDistance(leftSource, rightSource, destination): 
    result = dict()
    result['L'] = abs(leftSource[0] - destination[0]) + abs(leftSource[1] - destination[1])
    result['R'] = abs(rightSource[0] - destination[0]) + abs(rightSource[1] - destination[1])

    return result

def solution(number_arr, hand):
    answer = ''
    hand_abbreviations = {'right': 'R', 'left': 'L'}
    keypad = ['1','2','3','4','5','6','7','8','9','*','0','#']
    position = {'L': '*', 'R': '#'}

    coordinate = dict()
    for i in range(len(keypad)): 
        y, x = divmod(i, 3)
        coordinate[keypad[i]] = [x, y]

    for number in number_arr:
        if number in [1,4,7]: answer += 'L'
        elif number in [3,6,9]: answer += 'R'
        else: 
            distance = getDistance(coordinate[position['L']], coordinate[position['R']], coordinate[str(number)])
            if distance['L'] == distance['R']: answer += hand_abbreviations[hand] 
            else: answer += min(distance, key=distance.get)
        
        position[answer[-1]] = str(number)

    return answer




numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]	
hand = 'right'

print(solution(numbers, hand))