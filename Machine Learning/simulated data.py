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
