def findMaxNumber(a, b, c):
    if a > b:
        return a
    elif b > c:
        return b
    else:
        return c


print(findMaxNumber(1, 2, 3))
