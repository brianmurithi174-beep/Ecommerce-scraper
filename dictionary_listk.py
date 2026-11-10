import pandas as pd
fruit_protein ={
    "Avocado":2.0,
    "Guava": 2.6,
    "Blackberries": 2.0,
    "oranges" : 0.9,
    "Bananas": 1.1,
    "Apples": 0.3,
    "Kiwis":1.1,
    "pomegranate": 1.7,
    "Mango": 0.8,
    "cherries":1.0,
}
s2 = pd.Series(fruit_protein,name = "proteins")
s2["Mango"] = 2.8
print(s2)
import numpy as np

ser = pd.Series(['a',np.nan, 1, np.nan, 2])
print(ser.notnull().sum())