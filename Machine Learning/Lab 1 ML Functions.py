# lab 1 functions
import theta
from fontTools.ttLib.woff2 import base128Size

# 1 Implement ATA
# A = [1 2 3
#      4 5 6]


A = [[1, 2, 3], [4, 5, 6]]


def matrix_multiplication(matrix):
    rows_A = len(matrix)
    cols_A = len(matrix[0])
    A_T = []


    for j in range(cols_A):
        new_row = []
        for i in range(rows_A):
            new_row.append(matrix[i][j])
        A_T.append(new_row)

    return A_T
A_T = matrix_multiplication(A)

print("Transposed Matrix (A^T):")

# for row in A_T:

print(A_T)

# matric multiplication
for r in A_T:
    # r[0] is 1st item, r[1] is second item in A_T row
    # A[0][0], A[1][0] are first column of A
    val = (r[0] * A[0][0] + (r[1] * A[1][0]))
    print(val, end=" ")
print()

# column 2 - index 1 of A rows
for r in A_T:
    val = (r[0] * A[0][1] + (r[1] * A[1][1]))
    print(val, end=" ")
print()

# column 3 - index 2 of A rows
for r in A_T:
    val = (r[0] * A[0][1] + (r[1] * A[1][2]))
    print(val, end=" ")
print()

# 2) Implement y = 2x1 + 3 and plot x1, y [start=-100, stop=100, num=100]

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np
start = -100
stop = 100
num = 100

x1 = np.linspace(start, stop, num)


step_size = (stop-start)/(num -1)

x1_values = []
y_values = []


for i in range(num):
    x1 = -100 + (i * step_size)
    y = 2 * x1 + 3

    x1_values.append(x1)
    y_values.append(y)


plt.plot(x1_values, y_values, label="y = 2x1 + 3", color="red", linewidth=5)

# to set a text headline at the very top of your chart.
plt.title("Plot using Python For Loop")
plt.xlabel("x1")
plt.ylabel("y")

plt.axhline(0, color="black", linewidth=0.5, linestyle="--")

plt.axvline(0, color="black", linewidth=0.5, linestyle="--")

plt.grid(True)

plt.legend()
plt.show()

# 3) Implement y = 2x12 + 3x1 + 4 and plot x1, y in the range [start=-100, stop=100, num=100]
start = -100
stop = 100
num = 100

x1 = np.linspace(start, stop, num)

step_size = (stop-start)/(num -1)

x1_values = []
y_values = []


for i in range(num):
    x1 = -100 + (i * step_size)

    y = 2 * x1**2 + 3*x1 + 4

    x1_values.append(x1)
    y_values.append(y)

plt.plot(x1_values, y_values, label="y = 2 * x1^2 + 3*x1 + 4", color="red", linewidth=2)

# to set a text headline at the very top of your chart.
plt.title("Plot using Python For Loop")
plt.xlabel("x1")
plt.ylabel("y")

plt.axhline(0, color="black", linewidth=0.5, linestyle="--")

plt.axvline(0, color="black", linewidth=0.5, linestyle="--")

plt.grid(True)

plt.legend()
plt.show()


# 4) Implement Gaussian PDF - mean = 0, sigma = 15 in the range[start=-100, stop=100, num=100]

mu = 0
sigma = 15

start = -100
stop = 100
num = 100

x = np.linspace(start, stop, num)
gaussian = (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mu) / sigma)**2)
print(gaussian)

# 5) Implement y = x1^2, plot x1, y in the range [start=--10, stop=10, num=100]. Compute the value of derivatives at these points, x1 = -5, -3, 0, 3, 5.  What is the value of x1 at which the function value (y) is zero. What do you infer from this?

start = -10
stop = 10
num = 100

x1 = np.linspace(start, stop, num)

step_size = (stop-start)/(num -1)

x1_values = []
y_values = []


for i in range(num):
    x1 = -100 + (i * step_size)

    y = x1**2

    x1_values.append(x1)
    y_values.append(y)

# print(len(x1))



# 6) Implement y = 2x1 + 3x2 + 3x3 + 4, where x1, x2 and x3 are three independent variables. Compute the gradient of y at a few points and print the values.


def gradient_system(x1, x2, x3):

    y = 2 * x1 + 3 * x2 + 3 * x3 + 4


    dy_dx1 = 2
    dy_dx2 = 3
    dy_dx3 = 3

    return y, (dy_dx1, dy_dx2, dy_dx3)



points = [
    (1.0, 2.0, 3.0),
    (-5.0, 10.0, 0.0),
    (0.0, 0.0, 0.0)
]

for i, (x1, x2, x3) in enumerate(points, 1):
    y, gradients = gradient_system(x1, x2, x3)
    print(f"--- Point {i}: ({x1}, {x2}, {x3}) ---")
    print(f"y value: {y}")
    print(f"Gradients [dy/dx1, dy/dx2, dy/dx3]: {gradients}\n")

# 7) Here is a linear model.
# y = 2x1 + 3x2 + 3x3 + 4
# THe coefficients, represented as theta, is a vector given below
# 0 = [2 3 3 ]
# There are 5 samples represented as a matrix, X, given below
# x =
#       [1 0 2]
#       [0 1 1]
#       [2 1 0]
#       [1 1 1]
#       [0 2 1]
# compute X0 =

def compute_matrix():
    theta = [2, 3, 3]
    x =    [
       [1, 0, 2],
       [0, 1, 1],
       [2, 1, 0],
       [1, 1, 1],
       [0, 2, 1],
    ]
    result = []

    for row in x:
        row_output = (row[0] * theta[0] + (row[1] * theta[1]) + (row[2] * theta[2]))
        result.append(row_output)

    return result

output = compute_matrix()
print(f"The result of X*theta is: {output}")













