# Q1: Giá trị in ra là gì?
x = True
y = False
z = False
print(x or y and z)

Giá trị là False

x = 'de' not in 'abcd eded'
print(x)
Giá trị là False


x = 'Python'
y='python'
print(x==y)
print(x is y)
Giá trị là False


x = 10=='1'+'0'
print(x)
Giá trị là False

z = 2
y = 1
x = y < z or z > y and y > z or z < y
print(x)
Giá trị là True


w = 7
x = 3
y = 4
z = True
a = w + x * y
b = w + x / z
print(a ? b) => True

