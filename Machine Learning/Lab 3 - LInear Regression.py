# 1) Implement  linear regression model using scikit-learn for the simulated dataset - simulated_data_multiple_linear_regression_for_ML.csv - to predict the "disease_score" from multiple clinical parameters.

# i have taken a panda library; so import panda
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score


# pd.read.csv are panda function; and you can give slicing also
def load_data():
    df = pd.read_csv("simulated_data_multiple_linear_regression_for_ML.csv")
    # i have not taken disease_score and disease_score_fluct as it is "y"
    # so, i have taken only x = age, BMI,BP, blood sugar, gender
    # here you have to put [[]] double list; as the machine understands it is in single column; so if you put in double list machine knows that you are calling that & it is different columns
    x = df[["age","BMI","BP","blood_sugar","Gender"]]
    # "y" is my target; so, y = disease_score & disease_score_fluct; but at present i have done only disease_score
    # if you want disease_score_fluct just give y = df[disease_score_fluct]
    y = df["disease_score"]
    return x, y


def mymain():
    x,y = load_data()
    x_train, x_test, y_train, y_test = train_test_split (x,y, test_size=0.20, random_state=999)
    print("end")




    print('-----TRAINING-----')
    print("n = %d " % (len(x)))


    model = LinearRegression()

    model.fit(x_train, y_train)
    y_pred = model.predict(x_test)
    r2 = r2_score(y_test, y_pred)
    print(r2)


if __name__ == "__main__":
    mymain()

# 2) Implement a linear regression model using scikit-learn for the simulated dataset-simulated_data_multiple_linear_regression_for_ML.csv - to predict the "disease_score_fluct" from multiple clinical parameters.
def load_data():
    df = pd.read_csv("simulated_data_multiple_linear_regression_for_ML.csv")

    x = df[["age","BMI","BP","blood_sugar","Gender","disease_score"]]
    y = df["disease_score_fluct"]
    return x, y

def mymain():
    x,y = load_data()
    x_train, x_test, y_train, y_test = train_test_split (x,y, test_size=0.20, random_state=999)
    print("end")

    print('-----TRAINING-----')
    print("n = %d " % (len(x)))

    model = LinearRegression()

    model.fit(x_train, y_train)
    y_pred = model.predict(x_test)
    r2 = r2_score(y_test, y_pred)
    print(r2)


if __name__ == "__main__":
    mymain()

# 3) Use the above simulated CSV file and implement the following from scratch in python
# - Read simulated data csv files
# - Form x and y (disease_score_fluct)
# - Write a function to compute hypothesis
# - write a function to compute the cost
# - write a function to compute the derivatives
# - Write update parameters logic in the main function

# - Read simulated data csv files
def load_data():
    df = pd.read_csv("simulated_data_multiple_linear_regression_for_ML.csv")
    x = df[["age", "BMI", "BP", "blood_sugar", "Gender", "disease_score"]]
    y = df["disease_score_fluct"]
    return x, y


    print(df.head())
    print(df.tail())
    print(df.shape)
    print(df.info())
    print(df.describe())
# - Write a function to compute hypothesis
def hypothesis(theta0, theta1, x):
    h = theta0 + (theta1 * x)
    return h
result = hypothesis(10, 20, 50)
print(result)

# - write a function to compute the cost
# Formula: J(w) = (1 / 2m) * sum((h(x) - y)^2)
def compute_cost(X, y, weights):
    m = len(y)
    total_squared_error = 0.0
    for i in range(m):
        prediction = compute_cost(X[i], weights)
        error = prediction - y[i]
        total_squared_error += error ** 2
    return total_squared_error / (2 * m)

import numpy as np
def compute_derivative(X, y, theta):
    m = len(y)

    # Predicted values
    h = np.dot(X, theta)

    # Compute gradient
    derivative = (1/m) * np.dot(X.T, (h - y))

    return derivative

# Parameters
def main():

    theta = [0, 0, 0, 0, 0, 0, 0] # initialize parameters

    alpha = 0.000001 # learning rate
    iterations = 1000

    for i in range(iterations):

        derivative = compute_derivative(X, y, theta)

        # Update parameters
        for j in range(len(theta)):
            theta[j] = theta[j] - alpha * derivative[j]

    print("Final Theta:")
    print(theta)


