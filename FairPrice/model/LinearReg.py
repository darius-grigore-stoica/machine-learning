import pandas as pd
from sklearn.linear_model import LinearRegression

train_data = pd.read_csv('training_data.csv')
test_data = pd.read_csv('testing_data.csv')

X_train = train_data[['Camere', 'Dim', 'Cartier']]
y_train = train_data['Pret']

X_test = test_data[['Camere', 'Dim', 'Cartier']]
y_test = test_data['Pret']

regression_model = LinearRegression()
regression_model.fit(X_train, y_train)

y_predict = regression_model.predict(X_test)

from sklearn.metrics import r2_score, mean_squared_error

print('R-squared:', r2_score(y_test, y_predict))
print('MSE:', mean_squared_error(y_test, y_predict))