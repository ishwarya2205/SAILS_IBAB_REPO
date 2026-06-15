import pandas as pd
import numpy as np

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import KFold, cross_val_score

# Load Boston Housing CSV file
data = pd.read_csv("Boston.csv")

# Features (X)
X = data[['crim','zn','indus','chas','nox','rm',
          'age','dis','rad','tax','ptratio','lstat']]

# Target (y)
y = data['medv']

# Create Linear Regression model
model = LinearRegression()

# 10-Fold Cross Validation
kf = KFold(n_splits=10, shuffle=True, random_state=42)

# Compute R2 scores
r2_scores = cross_val_score(model,
                            X,
                            y,
                            cv=kf,
                            scoring='r2')

# Mean and Standard Deviation
mean_r2 = np.mean(r2_scores)
std_r2 = np.std(r2_scores)

print("R2 Scores for 10 folds:")
print(r2_scores)

print("\nMean R2 Score =", mean_r2)
print("Standard Deviation =", std_r2)