from math import pi
vec = [-4, -2, 0, 2, 4]
print([x*2 for x in vec])
print([x for x in vec if x >= 0])
print([(x, x**2) for x in range(6)])
print([str(round(pi, i)) for i in range(1, 6)])


# nested list_comprehension
#  transpose rows and columns:
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
print(a)
del a[3:4]
print(a)

