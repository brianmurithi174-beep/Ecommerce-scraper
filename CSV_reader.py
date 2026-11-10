# read write files .py
with open("industry.csv","r") as file:
    data = file.read()

with open("industry.csv","w") as file:
    file.write(data)