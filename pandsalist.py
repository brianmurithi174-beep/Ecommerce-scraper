import pandas as pd
s = pd.Series([10,20,30,40,50])
print(s)
print(s.index)
s.name = "calories"
print(s.name)
#i loc -> location based indexing
print(s.iloc[3]) # gives one value index
print(s.iloc[[1,3,4]])# gives multiple values of multiple indices
index = ["Apple","Banana","Mango","Orange","pineapple"]
s.index = index
print(s)
print(s["Apple"])
#label based indexing
print(s.loc["Mango"])
print(s["Banana":"pineapple"])# prints the first element to the last element