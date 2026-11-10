
""" Operations for writing and appending to files"""
#create a new file
opfile = open("output.csv", 'w')

#writing to the file
opfile.write(" writing to a new file.")

#To add a new line the new character must be used
opfile.write("\n second line ")

opfile.close()

#read and display the contents of the file
infile = open("output.csv")
print("\n read the original file:\n")
print(infile.read())
infile.close()

#reopen the file to add new file
opfile = open("output.csv", 'a')

opfile.write("\n Adding to the file.")
opfile.write("\n Adding another line.")

opfile.close()

infile = open("output.csv")
print("\n read the modified file:\n")
print(infile.read())
infile.close()

"""Processing a csv file"""
#open the csv file for reading
file_obj = open("C:\industry.csv")

#Rows are separated by new read character \n , so readlines() be used to read  them
csv_rows = file_obj.readlines()
list_csv = []

#Remove \n character from each row
for row in csv_rows:
    row = row.strip("\n")
    #strip using comas
    row = row.split(",")
    list_csv.append(row)
print(list_csv)

