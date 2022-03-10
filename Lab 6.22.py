# Lab 6.22
# Linh Pham - ID# 2027194
# This program identifies the solution to a set of equation. The user will enter values for variable and the program
# generate output for value x and y.


a = int(input())
b = int(input())
c = int(input())

d = int(input())
e = int(input())
f = int(input())

solution_found = False

for x in range(-10, 11):
    for y in range(-10, 11):
        if a * x + b * y == c and d * x + e * y == f:
            print(x, y)
            solution_found = True

if not solution_found:
    print("No solution")
