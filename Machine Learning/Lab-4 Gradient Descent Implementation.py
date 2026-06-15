# 1) Implement gradient descent algorithm from scratch using python
import numpy as np
import matplotlib.pyplot as plt

# Function
def f(x):
    return x**2

# Derivative (gradient)
def grad_f(x):
    return 2 * x

# Parameters
x = 8.0                # Initial point
learning_rate = 0.1
num_iterations = 50

# Store history
x_history = [x]
cost_history = [f(x)]

# Gradient Descent
for i in range(num_iterations):
    gradient = grad_f(x)
    x = x - learning_rate * gradient

    x_history.append(x)
    cost_history.append(f(x))

    print(f"Iteration {i+1}: x = {x:.6f}, f(x) = {f(x):.6f}")

# Plot cost vs iteration
plt.plot(cost_history)
plt.xlabel("Iteration")
plt.ylabel("Cost")
plt.title("Gradient Descent Convergence")
plt.show()

# 2) Implement stochastic gradient descent algorithm form sratch

import numpy as np

# Training data
X = np.array([1, 2, 3, 4, 5], dtype=float)
y = np.array([2, 4, 6, 8, 10], dtype=float)

# Initialize parameters
w = 0.0
b = 0.0

learning_rate = 0.01
epochs = 100

n = len(X)

# Stochastic Gradient Descent
for epoch in range(epochs):

    for i in range(n):

        # Prediction
        y_pred = w * X[i] + b

        # Error
        error = y_pred - y[i]

        # Compute gradients
        dw = 2 * error * X[i]
        db = 2 * error

        # Update parameters
        w = w - learning_rate * dw
        b = b - learning_rate * db

    print(f"Epoch {epoch+1}: Weight={w:.4f}, Bias={b:.4f}")

print("\nFinal Weight =", w)
print("Final Bias =", b)





# 3) Use your implementation and train ML models for both california housing and simulated datasets and compare your results with the scikit-learn models


# 4) Plot the data points and the obtained regression line from all three approaches and compare the outcome.





