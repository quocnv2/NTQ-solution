a = [1, 2, 5, 0, 'a', 89, 6, 27, 11, -2, 100, 56, 37, (1, 2), ['1,2,3']]

for item in a.copy():
    if 'a' in item:
        a.remove(item)
        break
print(a)
