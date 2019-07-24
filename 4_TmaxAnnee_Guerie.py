import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt


"""Le fichier à des tableaux: 29ans*31jours par block * nombre de villes
ville1: 0-899 de colonne1 """
#importer le fichier:
data = np.loadtxt(open("previMeteo.txt", "r"), delimiter=";", skiprows=56)

lieu = 1 #au bout de 900 lignes du fichier il changes Latitude et Longitude
        #on lui indique le n° de la ville qu'on a observé
nbAnnee = 30
nbJoursJanvier = 31

#récuperer la 4eme colonne:
allDays = data[nbAnnee*nbJoursJanvier*(lieu-1):nbAnnee*nbJoursJanvier*lieu, 0]
#nbAnnee*nbJours*(lieu-1)=point de depart pour le tableau
#nbAnnee*nbJours*lieu=point de fin pour le tableau
#0 = de la colonne 0 du fichier txt
days_X_Years = np.array_split(allDays, nbAnnee)

allMaxTemp = data[nbAnnee*nbJoursJanvier*(lieu-1):nbAnnee*nbJoursJanvier*lieu, 4] - 273.15 #convertir K en °C
maxTemp_X_Days = np.array_split(allMaxTemp, nbAnnee)

#test on affiche les Tmax et les jours de l'année 0
# print(days_X_Years[0])
# print(maxTemp_X_Days[0])

#test on affiche les Tmax et les jours de l'année 0
# print(days_X_Years[0] - 20210100) #pour avoir que le jour
# print(maxTemp_X_Days[0])

#créer une liste pour les jours du mois:
month = np.arange(1, nbJoursJanvier+1) #créer une liste de 1 à 31; +1 il ne prend pas en compte le dernier
monthes = np.tile(month, nbAnnee)
#tile = concatener n fois le meme tableau,

 #créer une liste pour les années:
year = np.arange(2021, 2051)
years = np.repeat(year, nbAnnee+1)
#repeat = il prend la meme valeur et il la repet n fois

#print (len(allMaxTemp), len(monthes), len(years))

#fig: creer une nouvelle figure qui englobe les graphs
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(years, monthes, allMaxTemp)

plt.show()