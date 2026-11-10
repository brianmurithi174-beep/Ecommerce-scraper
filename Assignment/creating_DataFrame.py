import pandas as pd

#"""DataFrame from a dictionary"""
#create a dictionary of columns
#data = {
 #   'Name':['Emma','Gireeja','sophia'],
 #   'Age':['20','21','23'],
  #  'City':['London','Paris','San Jose ' ]
  #  }
#df = pd.DataFrame(data)
#print(df)

   # """DataFrame from a list"""
    #create a list of rows
    #data = [['Emma','15','Dubai'],['Gireeja','30','London'],['Sophia','30','San Jose']]
    #data2 = [['summer','july','1','2000'],['summer','june','12','1990',],['Fall','september','3','2020'],['Winter','January','7','1998'],['Fall','October','20','2001'],['winter','February','28','2022']]
    #Define column labels
    #columns = ['Name','Age','City']
    #columns = ['Season','Month','Month-day','Year']
    #Create a dataframe from a list using column labels
    #df = pd.DataFrame(data2, columns = columns)
    #print(df.tail(3))
    #print(df.info())
    #print(df.iloc[2])


dataset_table1 = {
    'Hours': [1,2,3,4.5,5,6,7,8,9,10],
    'scores':[20,30,40,50,60,70,80,85,90,100]
}
data = pd.DataFrame(dataset_table1)
print(data)













