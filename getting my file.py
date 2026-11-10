import os

file_name = "correct_coastline_data.csv"
current_directory = os.getcwd()
files_in_dir = os.listdir(current_directory)

print(f"--- Python is running in this folder: {current_directory}")

if file_name in files_in_dir:
    print(f"--- SUCCESS: Found '{file_name}' in the list! ---")
    print(f"Full Path: {os.path.join(current_directory, file_name)}")
else:
    print(f"--- ERROR: '{file_name}' is NOT in the directory list. ---")
    print("\nFiles Python can see:")
    # Print the first 10 files in that folder for a quick check
    for file in files_in_dir[:10]:
        print(f"- {file}")