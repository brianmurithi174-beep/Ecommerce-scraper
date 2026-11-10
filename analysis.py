import pandas as pd
import os

days = {
    'Season':['summer','summer','fall','winter','fall','winter'],
    'month':['July','june','september','january','october','february'],
    'month-day':[7,6,9,1,10,2],
    'Year':[2000,1990,2020,1998,2001,2022],
}
df = pd.DataFrame(days)
print(df)

print(df.info())
print(df.value_counts('Season'))