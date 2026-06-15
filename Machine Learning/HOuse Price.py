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


