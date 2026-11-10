# Task 2: Area Calculator
import math  # Import math module for pi

print("--- Area Calculator ---")

# 1. Prompt user to enter dimensions [cite: 30]
try:
    # Dimensions for the trapezium
    length1 = float(input("Enter trapezium top length (a): "))
    length2 = float(input("Enter trapezium bottom length (b): "))
    height = float(input("Enter trapezium height (h): "))

    # Dimension for the circle
    radius = float(input("Enter circle radius (r): "))
except ValueError:
    print("Invalid input. Please enter numeric values for dimensions.")
    exit()

# 2. Calculate the areas [cite: 31]
# Area of Trapezium = 1/2 * (a + b) * h
area_trapezium = 0.5 * (length1 + length2) * height

# Area of Circle = pi * r^2
area_circle = math.pi * (radius ** 2)

# Area of Shaded Part = Area of Trapezium - Area of Circle
area_shaded = area_trapezium - area_circle

# 3. Display the calculations on the screen [cite: 32, 33]
print("\n--- Calculation Results ---")
# Using f-strings to format the output as required [cite: 33]
print(f"Area of Trapezium is: {area_trapezium:,.2f}")
print(f"Area of Circle is: {area_circle:,.2f}")
print(f"Area of Shaded Part is: {area_shaded:,.2f}")