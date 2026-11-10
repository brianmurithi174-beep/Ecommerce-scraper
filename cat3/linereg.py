from scipy import stats
import numpy as np
import matplotlib.pyplot as plt

#data
edu = np.array([1,4,2,3,6,5,10,7,9,8])
envo = np.array([3,4,1,7,5,2,6,5,10,9])

#apply linear regression to data
slope,intercept,r_value,p_value,std_err = stats.linregress(edu,envo)

print(slope,intercept)

#calculate regression line
line = []
X= range(1,11)
for x in X:
    line.append(slope* x + intercept)

#plot
plt.plot(X,line,'r')
plt.scatter(edu,envo,color='blue', marker = 'o')
plt.xlabel('education')
plt.ylabel('environmental awareness')
plt.title('linear regression line')
plt.xlim(0,11)
plt.ylim(0,11)
plt.grid()