def palindrome(str):
    lowerStr = str.lower().replace(" ", "")
    return lowerStr[::-1] == lowerStr

print(palindrome('ann a'))

# print((lambda str: str[::-1] == str) ('anna'))