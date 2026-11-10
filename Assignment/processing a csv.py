#import pandas as pd
#list_csv = {
    #'Title':['1984','Jane Eyre','Walden','Moby Dick'],
    #'Author':['George Orwell','Charlotte\ Bronte',' Henry David Thoreau', ' Herman Melville',],
    #'Pages':['268,352','168','538','132']}
#my_data = pd.DataFrame(list_csv)
#print(my_data)
#my_data.to_csv('list_CSV.csv', index=False)
#print("<<<<Success, DataFrame saved to csv!>>>>")
"""processing a csv """
#opening a csv for reading
file_obj = open('list_CSV.csv')

#rows are separated by a newline \n character by commas, so Read lines() can be used to read in all rows into a string list
csv_rows = file_obj.readlines()
list_csv = []

#remove \n character from each row and split by comma and save into a 2D structure
for row in csv_rows:
    #remove the \n character
    row = row.strip('\n')
    #split using commas
    cells = row.split(',')
    list_csv.append(cells)
#print result
print(list_csv)
print(list_csv[1][2])