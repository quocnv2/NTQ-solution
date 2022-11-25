a = [1, 2, 5, 0, 'a', 89, 6, 27, 11, -2, 100, 56, 37, (1, 2), ['1,2,3']]
a.remove(['1,2,3'])
a.remove((1, 2))
a.remove('a')

list_sum = [ele for ele in a if ele > 0 and ele % 2 == 0]
print(list_sum)

sum = 0

for i in list_sum:
    sum += i
print(sum)

sum2 = 0
list_not_sum = [ele for ele in a if ele > 0 and ele % 2 != 0]
print(list_not_sum)

for j in list_not_sum:
    sum2 += j
print(sum2)
