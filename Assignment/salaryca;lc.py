# Task 1: Salary Calculator

# 1. Get user input for employee details [cite: 21]
payroll_no = input("Enter Payroll Number: ")
name = input("Enter Name: ")
gender = input("Enter Gender: ")
job_group = input("Enter Job Group (J, K, L, or M): ").upper() # Use .upper() for easier matching
try:
    salary = float(input("Enter Salary: "))
except ValueError:
    print("Invalid salary. Please enter a numeric value.")
    exit()

# 2. Determine house allowance based on job group [cite: 18]
house_allowance = 0
if job_group == 'J':
    house_allowance = 5000
elif job_group == 'K':
    house_allowance = 5500
elif job_group == 'L':
    house_allowance = 6000
elif job_group == 'M':
    house_allowance = 6500
else:
    print(f"Warning: Job group '{job_group}' not recognized. House allowance set to 0.")

# 3. Calculate gross pay, taxes, and net pay [cite: 25, 26]
gross_pay = house_allowance + salary  # [cite: 25]
taxes = 0.12 * salary                 # [cite: 25]
net_pay = gross_pay - taxes           # [cite: 26]

# 4. Display employee's details and calculations [cite: 23]
print("\n--- Employee Salary Details ---")
print(f"Payroll Number: {payroll_no}")
print(f"Name:           {name}")
print(f"Gender:         {gender}")
print(f"Job Group:      {job_group}")
print(f"Basic Salary:   {salary:,.2f}")
print(f"House Allowance: {house_allowance:,.2f}")
print("---------------------------------")
print(f"Gross Pay:      {gross_pay:,.2f}")
print(f"Taxes (12%):    {taxes:,.2f}")
print(f"Net Pay:        {net_pay:,.2f}")
print("---------------------------------")