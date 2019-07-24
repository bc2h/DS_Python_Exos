import matplotlib.pyplot as plt
import numpy as np

data= np.loadtxt(open("DS_P5_PMeteo_Data.txt", "r"), delimiter=";", skiprows=56)  # 'r' read

lieu = 1
nbreAnnees = 30
nbreJoursJanvier = 31

allDays = data[(lieu-1)*nbreAnnees*nbreJoursJanvier:(lieu)*nbreAnnees*nbreJoursJanvier,0]
#ou recherche avec correspondance de la lattitude
# allDays = data[data[:,1] == 47.00570]

days_X_Years = np.array_split(allDays, nbreAnnees)

allMaxTemp = data[(lieu-1)*nbreAnnees*nbreJoursJanvier:(lieu)*nbreAnnees*nbreJoursJanvier,4]-273.15  #conversion kelvin > celsius
maxTemp_X_Days = np.array_split(allMaxTemp, nbreAnnees)

# Affiche les températures et jours de l'année 0
# print(days_X_Years[0])
# print(maxTemp_X_Days[0])

print(days_X_Years[0]-20210100)

# fig = plt.figure()
# ax = fig.gca(projection='3d')