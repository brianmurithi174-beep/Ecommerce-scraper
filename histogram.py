import matplotlib.pyplot as plt
import numpy as np
x = np.random.normal(170,20,250)
plt.hist(x, bins=15, color='skyblue', edgecolor='black')
plt.title("Normal Distribution of Heights")
plt.xlabel("Height (cm)")
plt.ylabel("Frequency")
plt.show()
plt.show()

x = np