import pandas as pd
#creating dataframe
data = {
    "Name":['Alice','john','zablon'],
    "Age":[20, 18, 27],
    "County":["Bungoma","Busia","vihiga"]

}
df = pd.DataFrame(data)
print(df)
count_column = df.shape[1]#counts columns
print(count_column)
count_rows= df.shape[0]
print(count_rows)