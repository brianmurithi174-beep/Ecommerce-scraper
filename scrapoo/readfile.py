import pandas as pd

#reading data frame
df_coastlines=pd.read_csv("C:/Users/hp/PycharmProjects/myhomework/correct_coastline_data.csv")
#showing data frame
print(df_coastlines)
df_coastlines.rename(columns = {"Location Location":"country"}, inplace= True)
print(df_coastlines)
