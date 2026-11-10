import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# 1. Setup Data
Homeprices = {
    "area": [2600, 3000, 3200, 3600, 4000],
    "price": [550000, 565000, 610000, 680000, 725000]
}

df = pd.DataFrame(Homeprices)

# 2. Prepare features (X) and target (y)
# We use double brackets [['area']] to get a 2D array automatically.
# This fixes the "reshape" error and the "np.array(['string'])" error.
X = df[['area']]
y = df['price']

# 3. Split the data (80% train, 20% test)
X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Train the model
model = LinearRegression()
model.fit(X_train, Y_train)

# 5. Make Predictions
# Predict for a specific value
price_predict = [[3200]]
single_predicted_price = model.predict(price_predict)[0]
print(f'Predicted price for 3200 sqft: ${single_predicted_price:,.2f}')
print("-" * 30)

# Predict for the whole dataset (to add to DataFrame and Plot)
df['Predicted_price'] = model.predict(X)

# 6. Calculate Error
df['Error'] = df['price'] - df['Predicted_price']

print("Data Frame with Error:")
print(df.round(2))
print("-" * 30)

# 7. Visualization
# We moved this to the END, because 'Predicted_price' didn't exist before.
plt.figure(figsize=(10, 6))

# Plot the actual data points
plt.scatter(df['area'], df['price'], color='green', marker='*', s=100, label='Actual Price')

# Plot the regression line
plt.plot(df['area'], df['Predicted_price'], color="blue", linewidth=2, label="Regression Line")

# Visualizing the residuals (Error)
for i in range(len(df)):
    plt.vlines(df['area'][i], df['price'][i], df['Predicted_price'][i], colors='red', linestyles='dotted')

plt.xlabel('Area (sqr ft)')
plt.ylabel('Price (USD)')
plt.title('Monroe Real House Prices vs Predicted Prices')
plt.legend()
plt.grid(True)
plt.show()
price_predict = [[3200]]
predicted_price = model.predict(price_predict )[0]
print(f'predicted price:{predicted_price:.2f}')
print()

#add details for other houses predicted prices
df['predicted_price'] = model.predict(X)

#calculate error = Actual price - predicted price
df['Error'] = df['price']-df['predicted_price']

#data frame with error column
print("data frame with error")
print(df.round(2))
print()

#