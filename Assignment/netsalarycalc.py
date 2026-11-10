# Task 1: Net-Salary Calculator

print("--- Dallas Company Ltd. Net-Salary Calculator ---")

# 1. Capture employee details [cite: 74]
payroll_no = input("Enter Payroll Number: ")
name = input("Enter Name: ")
gender = input("Enter Gender: ")
department = input("Enter Department: ")
try:
    basic_salary = float(input("Enter Basic Salary: "))
except ValueError:
    print("Invalid salary. Please enter a numeric value.")
    exit()

# 2. Define allowances and calculate Gross Pay [cite: 67, 70, 75]
house_allowance = 6500  # [cite: 67]
medical_allowance = 5500 # [cite: 67]
allowances = house_allowance + medical_allowance
gross_pay = basic_salary + allowances # [cite: 70]

# 3. Calculate deductions: NHIF and NSSF [cite: 68, 77]
NHIF= 0.02 * gross_pay  # 2% of gross pay [cite: 68]
NSSF = 0.03 * gross_pay  # 3% of gross salary (assumed gross pay) [cite: 68]

# 4. Calculate P.A.Y.E based on gross pay [cite: 72, 76]
paye = 0.0
if gross_pay > 49000:
    paye = 0.06 * gross_pay
elif 31000 <= gross_pay <= 39000:
    paye = 0.05 * gross_pay
elif 20000 <= gross_pay <= 30000:
    paye = 0.04 * gross_pay
elif 0 <= gross_pay <= 19000:
    paye = 0.0
# Note: The provided PAYE table [cite: 72] has gaps
# (e.g., 19,001-19,999, 30,001-30,999, 39,001-49,000).
# Pay in these ranges will default to PAYE 0.0 as per this logic.

# 5. Calculate Total Deductions and Net Pay [cite: 69, 70, 78]
total_deductions = paye + NHIF + NSSF # [cite: 69, 77]
net_pay = gross_pay - total_deductions # [cite: 70, 78]

# 6. Display all details in the specified format [cite: 79]
print("\n---------------------------------------------------------")
print(f"Name of employee: {name}  Payroll No: {payroll_no}  Gender: {gender}  Department: {department}")
print(f"Basic Pay: \t\t{basic_salary:,.2f}")
print(f"Gross Pay: \t\t{gross_pay:,.2f}") # Added Gross Pay for clarity
print("\n--- Deductions ---")
print(f"P.A.Y.E: \t\t{paye:,.2f}") # Added PAYE for clarity
print(f"NHIF: \t\t\t{NHIF:,.2f}")
print(f"NSSF: \t\t\t{NSSF:,.2f}")
print(f"Total Deductions: \t{total_deductions:,.2f}")
print("\n---------------------------------------------------------")
print(f"NET PAY: \t\t{net_pay:,.2f}")
print("---------------------------------------------------------")