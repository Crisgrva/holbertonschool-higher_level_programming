#!/usr/bin/python3
matrix_divided = __import__('2-matrix_divided').matrix_divided

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
print(matrix_divided(matrix, 3))
print(matrix)


print("------------------------")


matrix = 5
try:
    print(matrix_divided(matrix, 3))
except Exception as e:
    print(e)


print("------------------------")


matrix = [
    ["Hello", 4, 2],
    [4, 5, 6]
]
try:
    print(matrix_divided(matrix, 3))
except Exception as e:
    print(e)


print("------------------------")


matrix = [
    [1, 4, 2, 4],
    [4, 5, 6]
]
try:
    print(matrix_divided(matrix, 3))
except Exception as e:
    print(e)


print("------------------------")



matrix = [
    [1, 4, 2],
    [4, 5, 6]
]
try:
    print(matrix_divided(matrix, "Hello"))
except Exception as e:
    print(e)


print("------------------------")

matrix = [True, True]
try:
    print(matrix_divided(matrix, 3))
except Exception as e:
    print(e)


print("------------------------")

matrix = [None, None]
try:
    print(matrix_divided(matrix, 3))
except Exception as e:
    print(e)

