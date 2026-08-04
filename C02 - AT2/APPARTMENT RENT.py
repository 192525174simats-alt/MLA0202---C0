import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import mean_squared_error, r2_score

data = {
    'Floor_Area': [600, 800, 1000, 1200, 1500, 700, 900, 1100, 1300, 1600],
    'Rooms': [1, 2, 2, 3, 4, 2, 2, 3, 3, 4],
    'Location': ['A', 'A', 'B', 'B', 'C', 'A', 'B', 'C', 'C', 'C'],
    'Rent': [12000, 16000, 18000, 22000, 30000, 15000, 19000, 25000, 27000, 32000]
}

df = pd.DataFrame(data)

encoder = LabelEncoder()
df['Location'] = encoder.fit_transform(df['Location'])

X = df[['Floor_Area', 'Rooms', 'Location']]
y = df['Rent']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Actual Rent:", list(y_test))
print("Predicted Rent:", y_pred)

print("\nModel Performance")
print("R² Score:", r2_score(y_test, y_pred))
print("Mean Squared Error:", mean_squared_error(y_test, y_pred))

new_data = pd.DataFrame({
    'Floor_Area': [1400],
    'Rooms': [3],
    'Location': [encoder.transform(['C'])[0]]
})

predicted_rent = model.predict(new_data)

print("\nPredicted Rent for New Apartment: ₹{:.2f}".format(predicted_rent[0]))
