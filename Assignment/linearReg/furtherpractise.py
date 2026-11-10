from sklearn import datasets, linear_model
import numpy as np
import  matplotlib.pyplot as plt

#data
edu = np.array([1,4,2,3,6,5,10,7,9,8])
envo = np.array([3,4,1,7,5,2,6,5,10,9])

#transform to format as demanded by sklearn models
edu = [[x] for x in edu]
envo = [[y] for y in envo]

#define the ML - model to be used
regr = linear_model.LinearRegression()

#train the model
regr.fit(edu,envo)

#plot
plt.plot(edu,regr.predict(edu), color = 'red')
plt.scatter(edu,envo, color = 'blue', marker = '*')
plt.xlabel('Education')
plt.ylabel('environmental awareness')
plt.title('linear regression line')
plt.xlim(0,11)
plt.ylim(0,11)
plt.grid()
plt.show()