import matplotlib.pyplot as plt
import numpy as np

data= np.loadtxt(open("DS_P4_Meteo_Data.txt", "r"), delimiter=";", skiprows=2)  # 'r' read

date = data[:,0]
tMax = data[:,1]
tMin = data[:,2]

tMaxC = (tMax-32)*(5/9)
tMinC = (tMin-32)*(5/9)

tMoy = (tMaxC+tMinC)/2

tMinSC = np.array(np.array_split(tMinC, 2))
tMinS0C = tMinSC[0]
tMinS1C = tMinSC[1]

tMaxSC = np.array(np.array_split(tMaxC, 2))
tMaxS0C = tMaxSC[0]
tMaxS1C = tMaxSC[1]


tempAll= np.concatenate((tMinC, tMaxC))     # bien conserver les doubles (())
tempMax= tempAll.max()                      # ou np.max(tempAll)
tempMin= tempAll.min()                      # ou np.min(tempAll)
tempMoy= tempAll.mean()                     # ou np.mean(tempAll)
# print(tempMax, tempMin, tempMoy)

labels = ['LUN', 'MAR', 'MER', 'JEU', 'VEN', 'SAM', 'DIM']

plt.subplot(221)
plt.plot( np.arange(1,8), tMaxS0C, color='tab:red', label='Max')
plt.plot( np.arange(1,8), tMinS0C, color='tab:blue', label='Min')
plt.gca().set_ylim([tempMin-1,tempMax+10])
plt.title('Semaine du 9 au 15/07')
plt.legend(title="Température (°C)")

plt.subplot(222)
plt.plot( np.arange(1,8), tMaxS1C, color='tab:red', label='Max')
plt.plot( np.arange(1,8), tMinS1C, color='tab:blue', label='Min')
plt.gca().set_ylim([0,100])                                         #permet de récupérer l'objet des axes
plt.xticks(np.arange(1,8), labels, rotation=45)
plt.title('Semaine du 16 au 22/07')
plt.legend(title="Température (°C)")

plt.subplot(212)
plt.plot( date, tMoy , label='°c Moy')
plt.title('Température moyenne entre le 9 et 22/07')
plt.legend(title="Température (°C)")
plt.annotate('T° Moy:'+str('%.2f'%tempMoy)+'\nT°Max:'+str('%.2f'%tempMax)+'\nT°Min:'+str('%.2f'%tempMoy), xy=(20,22))

plt.tight_layout(pad=1, w_pad=.4, h_pad=0.5)
plt.show()