def palindrome(str):
    lowerSter = str.lower()
    return str[::-1] == str

print(palindrome('anna'))

print((lambda str: str[::-1] == str) ('anna'))