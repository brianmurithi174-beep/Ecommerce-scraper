import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error

# Data Preparation [cite: 106, 108]
data = {
    'Hours': [1, 2, 3, 4.5, 5, 6, 7, 8, 9, 10],
    'Scores': [20, 30, 50, 52, 60, 62, 70, 78, 85, 95]
}
df = pd.DataFrame(data)
print("--- Entire Dataset ---")
print(df)

# Summary Statistics [cite: 122, 123]
print("\nSummary Statistics:\n", df.describe())
print("\nMissing Values:\n", df.isnull().sum())

# Initial Visualization [cite: 110, 111]
plt.scatter(df['Hours'], df['Scores'], color='blue', label='Actual Scores')
plt.title('Hours Studied vs. Exam Scores')
plt.xlabel('Hours')
plt.ylabel('Scores')
plt.show()

# [cite: 114] Split the dataset
X = df[['Hours']]
y = df['Scores']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# [cite: 115] Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# [cite: 117, 118] Predict for 6.5 hours (Fixed to avoid UserWarning)
# We use a DataFrame to keep the feature name 'Hours' consistent
predict_data = pd.DataFrame({'Hours': [6.5]})
score_65 = model.predict(predict_data)
print(f"\nPrediction for 6.5 hours: {score_65[0]:.2f}")

# [cite: 119, 120, 121] Calculate Errors and add to DataFrame
df['Predicted Score'] = model.predict(df[['Hours']])
df['Error'] = df['Scores'] - df['Predicted Score']
print("\n--- Data with Predicted Scores and Error ---")
print(df)

# [cite: 124-130] Visualization with Regression Line
plt.scatter(df['Hours'], df['Scores'], color='blue', label='Actual Scores')
plt.scatter(df['Hours'], df['Predicted Score'], color='green', label='Predicted Scores', marker='x')
plt.plot(df['Hours'], df['Predicted Score'], color='red', label='Regression Line')
plt.title('Actual vs Predicted Student Performance')
plt.xlabel('Hours')
plt.ylabel('Scores')
plt.legend()
plt.show()


#multivariate linear regression
# [cite: 132, 133] Update dataset
df['Practice_Exams'] = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
print("\n--- Multivariate Dataset ---")
print(df[['Hours', 'Practice_Exams', 'Scores']])

# [cite: 134] Train Multivariate Model
X_multi = df[['Hours', 'Practice_Exams']]
model_multi = LinearRegression()
model_multi.fit(X_multi, y)

# [cite: 135] Predict for 6.5 hours and 3 practice exams
multi_predict_data = pd.DataFrame({'Hours': [6.5], 'Practice_Exams': [3]})
score_multi = model_multi.predict(multi_predict_data)
print(f"Predicted score (6.5 hrs, 3 exams): {score_multi[0]:.2f}")

#model evaluation and user interaction
# [cite: 137, 138] Compare Actual vs Predicted on Test Set
y_pred_test = model.predict(X_test)
comparison = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred_test})
print("\n--- Actual vs Predicted (Test Set) ---")
print(comparison)

# [cite: 140, 141] Evaluation Metrics
print(f"\nMean Absolute Error (MAE): {mean_absolute_error(y_test, y_pred_test):.2f}")
print(f"Mean Squared Error (MSE): {mean_squared_error(y_test, y_pred_test):.2f}")

# [cite: 142, 143] User Interaction Function
def get_prediction():
    try:
        user_hours = float(input("\nEnter study hours to predict score: "))
        user_input_df = pd.DataFrame({'Hours': [user_hours]})
        result = model.predict(user_input_df)
        print(f"Predicted Score: {result[0]:.2f}")
    except ValueError:
        print("Please enter a valid number.")

# Uncomment the line below to run the interaction
# get_prediction()
