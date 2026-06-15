import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score


def mymain():

    # Load dataset
    df = pd.read_csv("qc_batches_large.csv")

    # Convert dates
    df["Date"] = pd.to_datetime(df["Date"])
    df["Date Reviewed"] = pd.to_datetime(df["Date Reviewed"])

    # Create target variable
    df["Review_Days"] = (
        df["Date Reviewed"] - df["Date"]
    ).dt.days

    print("First 5 rows:")
    print(df.head())

    # Features
    X = df[
        [
            "Product Name",
            "Dosage Form",
            "Test Parameter",
            "Lab Section"
        ]
    ]

    # Convert categorical columns into numbers
    X = pd.get_dummies(X)

    # Target
    y = df["Review_Days"]

    # Train-test split
    x_train, x_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    # Linear Regression model
    model = LinearRegression()

    model.fit(x_train, y_train)

    # Predictions
    y_pred = model.predict(x_test)

    print("\nPredictions:")
    print(y_pred[:10])

    print("\nActual Values:")
    print(y_test.iloc[:10].values)

    # Evaluation
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    print("\nMean Squared Error:", mse)
    print("R2 Score:", r2)

    # Coefficients
    print("\nFeature Coefficients:")
    coeff_df = pd.DataFrame({
        "Feature": X.columns,
        "Coefficient": model.coef_
    })

    print(coeff_df)

if __name__ == "__main__":
    mymain()