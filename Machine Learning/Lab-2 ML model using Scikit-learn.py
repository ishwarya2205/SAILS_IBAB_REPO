# For a design or feature matrix,
x = [
    [1, 0, 2],
    [0, 1, 1],
    [2, 1, 0],
    [1, 1, 1],
    [0, 2, 1],
]

# Compute the covariance matrix using matrix multiplications. Verify your results by using numpy library operations.
import numpy as np

# 1. Define a sample dataset (5 observations, 3 variables)
X = np.array([
    [4.0, 2.0, 0.6],
    [4.2, 2.1, 0.59],
    [3.9, 2.0, 0.58],
    [4.3, 2.3, 0.62],
    [4.1, 2.2, 0.61]
])

# 2. Extract dimensions
n = X.shape[0]  # Number of rows (observations)

# 3. Mean-center the columns of the data matrix
X_centered = X - np.mean(X, axis=0)

# 4. Compute using manual matrix multiplication (Dot Product)
cov_matrix_manual = (X_centered.T @ X_centered) / (n - 1)

# 5. Verify results using built-in NumPy library function
# rowvar=False states that columns represent variables/features
cov_matrix_numpy = np.cov(X, rowvar=False)

# Print and cross-check outputs
print("--- Matrix Multiplication Approach ---")
print(cov_matrix_manual)

print("\n--- NumPy Built-in Approach ---")
print(cov_matrix_numpy)

print("\nAre the results identical?", np.allclose(cov_matrix_manual, cov_matrix_numpy))

# wihtout numpy
# 1. Define a sample dataset (5 observations, 3 variables)
X = [
    [4.0, 2.0, 0.6],
    [4.2, 2.1, 0.59],
    [3.9, 2.0, 0.58],
    [4.3, 2.3, 0.62],
    [4.1, 2.2, 0.61]
]

n = len(X)  # Number of rows (observations)
m = len(X[0])  # Number of columns (variables)

# 2. Compute the mean of each column
column_means = []
for col in range(m):
    col_sum = sum(X[row][col] for row in range(n))
    column_means.append(col_sum / n)

# 3. Mean-center the matrix (X_centered = X - Mean)
X_centered = []
for row in range(n):
    centered_row = [X[row][col] - column_means[col] for col in range(m)]
    X_centered.append(centered_row)

# 4. Transpose the mean-centered matrix (X_centered^T)
# This swaps rows and columns to prepare for dot-product multiplication
X_centered_T = []
for col in range(m):
    transposed_row = [X_centered[row][col] for row in range(n)]
    X_centered_T.append(transposed_row)

# 5. Matrix Multiplication (X_centered_T @ X_centered) and divide by (n - 1)
cov_matrix = []
for i in range(m):
    cov_row = []
    for j in range(m):
        # Calculate dot product of row i from Transposed and column j from Centered
        dot_product = sum(X_centered_T[i][k] * X_centered[k][j] for k in range(n))

        # Apply Bessel's correction factor for sample covariance (n - 1)
        covariance_value = dot_product / (n - 1)
        cov_row.append(covariance_value)
    cov_matrix.append(cov_row)

# 6. Display the final covariance matrix formatted nicely
print("--- Final Covariance Matrix (Pure Python) ---")
for row in cov_matrix:
    print([round(val, 6) for val in row])

# 3) Compute the dot product of two vectors, x and y given below x = [2 1 2]**T and y = [1 2 2]**T. What is the meaning of the dot product of two vectors?
# Illustrate that with your own example.

x = [2, 1, 2]
y = [1, 2, 2]

dot_product = 0
for i in range(len(x)):
    dot_product += x[i] * y[i]
print(f"The dot product is {dot_product}")


# Implement california housing prediction model using scikit-learn - walkthro’ of bdbp207_californiahousing.py

# this is ML pipeline code; everytime just paste this code
# someone has build this code for us
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
def load_data():
    [X,y] = fetch_california_housing(return_X_y=True)
    return(X,y)


def mymain():
# load california housing dataset
    [X,y] = load_data()
    # split data - train: 70%, TEST: 30%
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=999)
    print("End")


# train a model
    print('----TRAINING----')
    print("N = %d " % (len(X)))

# training a linear regression
    model = LinearRegression()
# train the model
# we have given both x & y because it has to be trained in a supervised manner
    model.fit(X_train, y_train)

# prediction on a test set
# y pred is the prediction we need & we have give x test data to get the y prediction
    y_pred = model.predict(X_test)


# compute the r2 score (performance measure - finally it gives number; give close to 1 - model is good; value is far away then the model is not good)
    r2 = r2_score(y_test, y_pred)
    print("r2 score is %0.2f (closer to 1 is good) " %r2)
    print('done!')


if __name__ == "__main__":
    mymain()

# Complete the following tutorial
# a. https://inria.github.io/scikit-learn-mooc/python_scripts/datasets_california_housing.html

from sklearn.datasets import fetch_california_housing
california_housing = fetch_california_housing(as_frame=True)

print(california_housing.DESCR)

california_housing.frame.head()
california_housing.data.head()
california_housing.target.head()
california_housing.frame.info()


import matplotlib.pyplot as plt

california_housing.frame.hist(figsize=(12, 10), bins=30, edgecolor="black")
plt.subplots_adjust(hspace=0.7, wspace=0.4)

features_of_interest = ["AveRooms", "AveBedrms", "AveOccup", "Population"]
california_housing.frame[features_of_interest].describe()

import seaborn as sns

sns.scatterplot(
    data=california_housing.frame,
    x="Longitude",
    y="Latitude",
    size="MedHouseVal",
    hue="MedHouseVal",
    palette="viridis",
    alpha=0.5,
)
plt.legend(title="MedHouseVal", bbox_to_anchor=(1.05, 0.95), loc="upper left")
_ = plt.title("Median house value depending of\n their spatial location")


import numpy as np

rng = np.random.RandomState(0)
indices = rng.choice(
    np.arange(california_housing.frame.shape[0]), size=500, replace=False
)

sns.scatterplot(
    data=california_housing.frame.iloc[indices],
    x="Longitude",
    y="Latitude",
    size="MedHouseVal",
    hue="MedHouseVal",
    palette="viridis",
    alpha=0.5,
)
plt.legend(title="MedHouseVal", bbox_to_anchor=(1.05, 1), loc="upper left")
_ = plt.title("Median house value depending of\n their spatial location")

import pandas as pd

# Drop the unwanted columns
columns_drop = ["Longitude", "Latitude"]
subset = california_housing.frame.iloc[indices].drop(columns=columns_drop)
# Quantize the target and keep the midpoint for each interval
subset["MedHouseVal"] = pd.qcut(subset["MedHouseVal"], 6, retbins=False)
subset["MedHouseVal"] = subset["MedHouseVal"].apply(lambda x: x.mid)


_ = sns.pairplot(data=subset, hue="MedHouseVal", palette="viridis")

from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import RidgeCV
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import cross_validate

alphas = np.logspace(-3, 1, num=30)
model = make_pipeline(StandardScaler(), RidgeCV(alphas=alphas))
cv_results = cross_validate(
    model,
    california_housing.data,
    california_housing.target,
    return_estimator=True,
    n_jobs=2,
)

score = cv_results["test_score"]
print(f"R2 score: {score.mean():.3f} ± {score.std():.3f}")


import pandas as pd

coefs = pd.DataFrame(
    [est[-1].coef_ for est in cv_results["estimator"]],
    columns=california_housing.feature_names,
)

color = {"whiskers": "black", "medians": "black", "caps": "black"}
coefs.plot.box(vert=False, color=color)
plt.axvline(x=0, ymin=-1, ymax=1, color="black", linestyle="--")
_ = plt.title("Coefficients of Ridge models\n via cross-validation")


