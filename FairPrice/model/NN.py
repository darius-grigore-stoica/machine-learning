import tensorflow as tf
from tensorflow import keras

import pandas as pd
from sklearn.model_selection import train_test_split

train_data = pd.read_csv('training_data.csv')
X_train = train_data[['Camere', 'Dim', 'Cartier']]
y_train = train_data['Pret']


test_data = pd.read_csv('testing_data.csv')
X_test = test_data[['Camere', 'Dim', 'Cartier']]
y_test = test_data['Pret']

model = keras.Sequential()
model.add(keras.layers.Dense(64, input_dim=3, activation='relu'))
model.add(keras.layers.Dense(32, activation='relu'))
model.add(keras.layers.Dense(16, activation='relu'))
model.add(keras.layers.Dense(1))

model.compile(loss='mean_squared_error', optimizer='adam', metrics=['mse'])
history = model.fit(X_train, y_train, epochs=100, batch_size=32, validation_split=0.2)
loss, mse = model.evaluate(X_test, y_test)
print('Mean Squared Error:', mse)

new_data = [[2,52,6.5]]
prediction = model.predict(new_data)
print('Predicted Price:', prediction)

