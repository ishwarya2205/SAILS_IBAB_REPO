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