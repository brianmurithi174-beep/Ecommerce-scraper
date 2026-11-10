# Task 2: Import required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error

print("Libraries imported successfully.\n")

# Task 3: Create dataset manually using dictionary and convert to DataFrame
data = {
    "Hours": [1, 2, 3, 4.5, 5, 6, 7, 8, 9, 10],
    "Scores": [20, 30, 50, 52, 60, 62, 70, 78, 85, 95]  # Fixed column name: "Scores" not "scores"
}

df = pd.DataFrame(data)

# Display the entire dataset
print("=== Dataset (Table 1) ===")
print(df)
print()

# Visualize data using scatter plot
plt.figure(figsize=(8, 5))
plt.scatter(df["Hours"], df["Scores"], color="blue", label="Actual Scores")
plt.title("Student Study Hours vs Exam Scores")
plt.xlabel("Hours Studied")
plt.ylabel("Exam Scores")
plt.legend()
plt.grid(True)
plt.show()

# Prepare features and target for Linear Regression
X = df[["Hours"]]    # 2D array required by sklearn
y = df["Scores"]

# Split into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Task 8 & 9: Predict score for a student who studies 6.5 hours
hours_to_predict = [[6.5]]
predicted_score = model.predict(hours_to_predict)[0]

print(f"Predicted Score for 6.5 hours of study: {predicted_score:.2f}")
print()

# Add predicted scores for all students in the dataset
df["Predicted_Score"] = model.predict(X)

# Calculate Error = Actual Score - Predicted Score
df["Error"] = df["Scores"] - df["Predicted_Score"]

# Display DataFrame with Error column
print("=== DataFrame with Predicted Scores and Errors ===")
print(df.round(2))  # Nice formatting
print()

# Task 12: Summary statistics
print("=== Summary Statistics ===")
print(df.describe())
print()

# Task 13: Check for missing/null values
print("=== Missing Values Check ===")
print(df.isnull().sum())
print("No missing values found.\n")

# Task 14–19: Plot actual vs predicted with regression line
plt.figure(figsize=(10, 6))
plt.scatter(df["Hours"], df["Scores"], color="blue", label="Actual Scores", s=100)
plt.scatter(df["Hours"], df["Predicted_Score"], color="red", marker="x", s=100, label="Predicted Scores")
plt.plot(df["Hours"], df["Predicted_Score"], color="green", linewidth=2, label="Regression Line")

plt.title("Hours vs Scores: Actual vs Predicted")
plt.xlabel("Hours Studied")
plt.ylabel("Exam Scores")
plt.legend()
plt.grid(True)
plt.show()

# Task 20–23: Multivariate Linear Regression (add Practice_Exams)
practice_exams = [1, 2, 2, 3, 3, 3, 4, 4, 5, 5]  # Realistic hypothetical values
df["Practice_Exams"] = practice_exams

print("=== Updated DataFrame with Practice Exams ===")
print(df[["Hours", "Practice_Exams", "Scores"]])
print()

# Train multivariate model
X_multi = df[["Hours", "Practice_Exams"]]
y_multi = df["Scores"]

X_train_m, X_test_m, y_train_m, y_test_m = train_test_split(X_multi, y_multi, test_size=0.2, random_state=42)

model_multi = LinearRegression()
model_multi.fit(X_train_m, y_train_m)

# Predict for 6.5 hours and 3 practice exams
pred_multi = model_multi.predict([[6.5, 3]])[0]
print(f"Predicted Score (6.5 Hours + 3 Practice Exams): {pred_multi:.2f}")
print()

# Task 24–26: Model Evaluation on Test Set (Multivariate)
y_pred_m = model_multi.predict(X_test_m)

comparison_df = pd.DataFrame({
    "Actual Score": y_test_m.values,
    "Predicted Score": y_pred_m
}).round(2)

print("=== Actual vs Predicted (Test Set - Multivariate) ===")
print(comparison_df)
print()

mae = mean_absolute_error(y_test_m, y_pred_m)
mse = mean_squared_error(y_test_m, y_pred_m)

print(f"\nModel Evaluation Metrics:")
print(f"Mean Absolute Error (MAE): {mae:.2f}")
print(f"Mean Squared Error (MSE):  {mse:.2f}")
print()

# Task 27: User Interaction Function (Simple model - Hours only)
# Task 27: User Interaction Function
def predict_student_score():
    print("\nStudent Score Predictor (Based on Study Hours)")
    try:
        hours = float(input("Enter number of study hours: "))
        if hours < 0:
            print("Hours cannot be negative!")
            return
        prediction = model.predict([[hours]])[0]
        print(f"Predicted Exam Score: {prediction:.2f}/100")
    except ValueError:
        print("Please enter a valid number.")

# Uncomment the next line if you want to test the function
# predict_student_score()

print("\n" + "="*50)
print("ALL 27 TASKS COMPLETED SUCCESSFULLY!")
print("You can now take screenshots of the plots and output.")
print("="*50)

# THIS LINE IS VERY IMPORTANT FOR PyCharm
input("\nPress ENTER to close the program...")