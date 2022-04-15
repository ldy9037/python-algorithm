num_arr = input('연속된 숫자 입력').split()

def compare_num(a, b):
    if a > b:
        print('a > b')
    elif a < b:
        print('a < b')
    elif a == b:
        print('a == b')

compare_num(int(num_arr[0]), int(num_arr[1]))
