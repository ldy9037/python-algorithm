from unittest import result


def triple(x):
    result = x

    for i in range(2):
        result += x 

    print(result)

triple(2)
triple('x')