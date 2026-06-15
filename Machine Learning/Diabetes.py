from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

def load_data():
    [X,y] = load_diabetes(return_X_y= True)
    return(X,y)



def mymain():
    X,y = load_data()
    X_train, X_test, y_train, y_test = train_test_split (X,y, test_size=0.20, random_state=999)
    print("End")




    print('-----TRAINING-----')
    print("N = %d " % (len(X)))

    model = LinearRegression()

    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)



    r2 = r2_score(y_test, y_pred)
    print("r2 score is %0.2f (closer to 1 is good) " %r2)
    print('done!')


if __name__ == "__main__":
    mymain()

from sklearn import datasets
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import KFold, cross_val_score
import numpy as np


def load_data():
    diabetes_X, diabetes_y = datasets.load_diabetes(return_X_y=True)

    diabetes_X = diabetes_X[:, 2].reshape(-1, 1)

    return diabetes_X, diabetes_y


def mymain():
    X, y = load_data()

    print("-----DATASET-----")
    print("N = %d" % len(X))

    model = LinearRegression()

    kfold = KFold(n_splits=10, shuffle=True, random_state=999)

    r2_scores = cross_val_score(
        model,
        X,
        y,
        cv=kfold,
        scoring='r2'
    )

    print("\n-----10-FOLD CROSS VALIDATION-----")
    print("R2 Scores:")
    print(r2_scores)

    print("\nMean R2 Score = %0.4f" % np.mean(r2_scores))
    print("Standard Deviation = %0.4f" % np.std(r2_scores))

    print("\ndone!")


if __name__ == "__main__":
    mymain()