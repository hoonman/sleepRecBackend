import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

def train_and_predict(input_data):
    df = pd.read_csv('sleep_stress.csv')

    features = ['Age', 'Sleep Duration', 'Physical Activity Level', 'Stress Level', 'Heart Rate', 'Daily Steps']
    target = 'Quality of Sleep'

    X = df[features]
    y = df[target]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    best_model = RandomForestRegressor(random_state=42)
    best_model.fit(X_train, y_train)

    y_pred = best_model.predict(X_test)

    mse = mean_squared_error(y_test, y_pred)
    print(f'Mean Squared Error: {mse}')

    input_array = np.array([[input_data['Age'], input_data['Sleep Duration'], input_data['Physical Activity Level'],
                             input_data['Stress Level'], input_data['Heart Rate'], input_data['Daily Steps']]])

    predicted_quality = best_model.predict(input_array)
    print("Predicted quality: ", predicted_quality[0])
    return predicted_quality[0]

input_data = {"Age": 30, "Sleep Duration": 7, "Physical Activity Level": 3, "Stress Level": 5, "Heart Rate": 70, "Daily Steps": 8000}
print(train_and_predict(input_data))
