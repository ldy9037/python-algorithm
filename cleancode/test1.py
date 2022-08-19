def test_function(value1:int, value2:str=None) -> dict:
    """두 개의 값을 전달 받아 dict으로 반환"""
    return {"v1": value1, "v2": value2}

print(test_function.__annotations__)
print(test_function.__doc__)