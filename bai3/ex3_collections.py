dicts = {'1': 'Python', '2': 'Basic', '3': 'NTQ'}

resultNewList = [(key) for key in dicts.keys()]
resultNewList2 = [(value) for value in dicts.values()]
print(resultNewList)
print(resultNewList2)

# print(resultNewList)
""" Nối các input
"""

newlissist = " ".join(resultNewList2)
print(newlissist)

""" Tinn tong cac list vua ghep """

new_number = [int(i) for i in resultNewList]
show_number = " ".join(resultNewList)
print(show_number)
print(sum(new_number))
