# Task 2: Disease Diagnosis Program

# 1. Display welcome message [cite: 85]
print("WELCOME TO JESHI HOSPITAL!")
print("\n")

# 2. Capture patient's personal details [cite: 86]
print("Enter your Personal Details:")
name = input("Name: ")
gender = input("Gender: ")
age = input("Age: ")
residence = input("Place of Residence: ")
print("\n")

# 3. Capture patient's symptoms [cite: 87]
print("Enter your Symptoms:")
# Use .lower() and .strip() to make matching easier and more reliable
symptom1 = input("Symptom 1: ").lower().strip()
symptom2 = input("Symptom 2: ").lower().strip()
print("\n")

# 4. Use entered symptoms to determine the possible diagnosis [cite: 83, 88]
diagnosis = "Unknown" # Default diagnosis

# Check for combinations, ignoring order
if (symptom1 == "vomiting" and symptom2 == "diarrhea") or \
   (symptom1 == "diarrhea" and symptom2 == "vomiting"):
    diagnosis = "Typhoid" # [cite: 83]
elif (symptom1 == "vomiting" and symptom2 == "fever") or \
     (symptom1 == "fever" and symptom2 == "vomiting"):
    diagnosis = "Malaria" # [cite: 83]
elif (symptom1 == "chest pain" and symptom2 == "wheezing sound") or \
     (symptom1 == "wheezing sound" and symptom2 == "chest pain"):
    diagnosis = "Pneumonia" # [cite: 83]
elif (symptom1 == "frequent urination" and symptom2 == "fluctuations of sugar levels") or \
     (symptom1 == "fluctuations of sugar levels" and symptom2 == "frequent urination"):
    diagnosis = "Diabetes" # [cite: 83]
else:
    diagnosis = "Inconclusive. Please consult a doctor for a full check-up."

# 5. Display the output in the specified format [cite: 89, 90]
print(f"Based on the symptoms, you could be suffering from {diagnosis}.")
print("Visit us for medication!")