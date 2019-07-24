import matplotlib.pyplot as plt
import numpy as np

data= np.loadtxt(open("DS_P3_Astro_Data.txt", "rb"), delimiter=",", skiprows=1)

data2 = data[:2000]

#moyenne mobile tout les 50 points
nbPack = 50
xMoy = np.array(np.array_split(data2[:,0], nbPack))
yMoy = np.array(np.array_split(data2[:,1], nbPack))

#deviation standard
devStd = np.std(yMoy, 1)

xPoints = xMoy.mean(axis=1)
yPoints = yMoy.mean(axis=1)

print(yPoints.size)

ya = yPoints+devStd
yb = yPoints-devStd

print(ya)

ax1 = plt.subplot(2,1,1)
ax1.scatter(data[:,0], data[:,1])

ax2 = plt.subplot (2,1,2, sharex=ax1)
ax2.plot(xPoints, yPoints, color='tab:orange')
ax2.errorbar(xPoints, yPoints, devStd, fmt='r')  #fmt = format = red
ax1.grid(True)
ax2.grid(True)
plt.show()