import matplotlib.pyplot as plt
import numpy as np

data= np.loadtxt(open("DS_P4_Meteo_Data.txt", "r"), delimiter=";", skiprows=2)  # 'r' read

xDate = data[:,0]
xDateS1 = data[:6,0]
xDateS2 = data[7:,0]
yMax = data[:,1]
yMaxS1 = data[:6,1]
yMaxS2 = data[7:,1]
yMin = data[:,2]
yMinS1 = data[:6,1]
yMinS2 = data[7:,1]

f1 = plt.subplot(1,1,1)
f1.plot(xDateS1, ((yMaxS1-32*(5/9))), color='tab:red')
f1.plot(xDateS1, ((yMinS1-32*(5/9))), color='tab:blue')

# f2 = plt.subplot (2,2,2, sharex=f1)
# f2.plot(xDateS2, ((yMaxS2-32*(5/9))), color='tab:red')
# f2.plot(xDateS2, ((yMinS2-32*(5/9))), color='tab:blue')
#
# # f3 = plt.subplot (1,1,1, sharex=f1)
# # f3.plot(xDate, ((yMax-32*(5/9))), color='tab:red')
# # f3.plot(xDate, ((yMin-32*(5/9))), color='tab:blue')
# f1.grid(True)
# f2.grid(True)
plt.show()

# plt.subplots_adjust(top=20, bottom=0.08, left=0.10, right=0.95, hspace=0.25, wspace=0.35)