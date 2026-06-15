# car price prediction project
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score

# load dataset
data = pd.read_csv(quot;car data.csv&quot;)

# show first 5 rows
print(data.head())

# check dataset info
print(data.info())

# convert categorial data into numerical data
data.replace({
&#39;Fuel_Type&#39;: {&#39;Petrol&#39;:0, &#39;Diesel&#39;:1, &#39;CNG&#39;:2},
&#39;Seller_Type&#39;: {&#39;Dealer&#39;:0, &#39;Individual&#39;:1},
&#39;Transmission&#39;: {&#39;Manual&#39;:0, &#39;Automatic&#39;:1}
}, inplace=True)

# create input features (X)
X = data.drop([&#39;Car_Name&#39;, &#39;Selling_Price&#39;], axis=1)

# create target variable (y)
y = data[&#39;selling_Price&#39;]

# split dataset into training and testing
X_train, X_test, y_train, y_test = train_test_split(
X, y, test_size=0.2, random_state=42
)

# create model
model = RandomForestRegressor()

# Train model
model.fit(X_train, y_train)

# predict prices
predictions = model.predict(X_test)

# Show predictions
print(&quot;\npredicted prices:&quot;)
print(predictions[:10])

# show actual prices
print(&quot;\nactual prices:&quot;)
print(y_test.values[:10])

# Accuracy score
r2 = r2_score(y_test, predictions)
print(&quot;Men Absolute Error:&quot;, mae)

# compute the r2 score
r2 = r2_score(y_test, y_pred)
print(&#39;done!&#39;)

if __name__ == &quot;__main__&quot;:
mymain()