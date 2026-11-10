import numpy as np
from markdown_it.rules_core import inline
from sklearn.svm  import SVR
import matplotlib as plt
#matplotlib inline
import matplotlib.pyplot as plt

#generate data
x = np.sort(5* np.random.rand(40,1), axis = 0)
y = np.cos(x).ravel()

#add noise to targets
y[::5] += 5 * (0.5 - np.random.rand(8))

#SVM regression
svr_rbf = SVR(kernel = 'rbf', C = 1e3, gamma=0.1)
y_rbf = svr_rbf.fit(x,y).predict(x)

plt.scatter(x, y, color = 'red', label='data')
plt.plot (x,y_rbf, 'b', lw = 2 , label = 'model')
plt.xlabel('data')
plt.ylabel('target')
plt.xlim(0,5)
plt.title('support vector regression')
plt.legend()
plt.grid()
plt.show()