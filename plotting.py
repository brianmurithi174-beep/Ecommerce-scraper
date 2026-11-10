import matplotlib.pyplot as plt
import numpy as np
#creating a s simple line graph


x =np.array(["A","B","C","D"])
y = np.array([10,20,5,2])

plt.barh(x,y, color = "green")
plt.show()