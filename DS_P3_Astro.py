import matplotlib.pyplot as plt
import numpy as np

# https://numpy.org/devdocs/user/quickstart.html

date, flux, error = [],[], []
with open("DS_P3_Astro_Datab.txt", "r") as f_read:
    for line in f_read:
        line = line.strip()
        # line = line.split(',')
        # print(line)
        if line :
            dateL, fluxL , errorL = [float(elt) for elt in line.split(',')]
            date.append(dateL), flux.append(fluxL), error.append(errorL)

# # nuage de points
print(date, flux, error)
plt.plot(date, flux, 'bo')
plt.show()

# avec erreurs
# plt.errorbar(date, flux, yerr=error, color='tab:grey')
# plt.show()

# ax = plt.subplots()
# ax.plot(date, flux, 'bo')
# ax.errorbar(date, flux, yerr=error, color='tab:grey')
# ax.grid(True)
# plt.show()