import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import title

y = np.array([20,40,15,70])
mylabels = ['A','B','C','D']
mycolors = ['green','blue','red','pink']
plt.pie(y,labels=mylabels, colors= mycolors)
plt.legend(title= 'four labels')

plt.show()