import sys
from PySide2.QtWidgets import (QLabel, QApplication,
    QVBoxLayout, QWidget, QComboBox, QHBoxLayout, QSizePolicy)
from PySide2.QtGui import QPixmap
import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO
import base64

class Voyage(QWidget):

    def __init__(self, parent=None):
        super(Voyage, self).__init__(parent)
        self.data = np.loadtxt(open("DS_P6_Voyage_Data.txt", "r"), delimiter=";", skiprows=1, dtype='str')

        self.cbCompagnie = QComboBox()
        self.cbCompagnie.currentIndexChanged.connect(self.updateDestinations)
        self.cbDestination = QComboBox()
        self.cbDestination.currentIndexChanged.connect(self.updateCourbe)
        self.imgCourbe = QLabel()
        self.imgCourbe.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        genLayout = QHBoxLayout()
        layoutCombo = QVBoxLayout()

        layoutCombo.addWidget(self.cbCompagnie)
        layoutCombo.addWidget(self.cbDestination)

        genLayout.addLayout(layoutCombo)
        genLayout.addWidget(self.imgCourbe)
        self.setLayout(genLayout)

        self.updateCompagnie()


    def updateCompagnie(self):
        companies = np.unique(self.data[:,0])
        self.cbCompagnie.addItems(companies)

    def updateDestinations(self):
        print("updateDestinations")
        self.cbDestination.clear()                      # vide la comboBox pour y afficher du nouveau contenu après
        companie = self.cbCompagnie.currentText()

        filtre1 = self.data[self.data[:,0]==companie]   # conserve tous les éléments sur lignes contenant la compagnie selectionnée
        destinations = filtre1[:, 4]
        self.cbDestination.addItems(np.unique(destinations))
        self.updateCourbe()

    def updateCourbe(self):
        companie = self.cbCompagnie.currentText()
        filtre1 = self.data[self.data[:, 0] == companie]

        destination = self.cbDestination.currentText()
        filtre2 = filtre1[filtre1[:,4]==destination]

        tarifs = filtre2[:,1]

        plt.plot(tarifs)

        plt.savefig('tutu.png', format='png')           # creation d'un fichier temporaire
        self.imgCourbe.setPixmap('tutu.png')
        plt.clf()


if __name__ == '__main__':
    # Create the Qt Application
    app = QApplication(sys.argv)
    # Create and show the form
    voy = Voyage()
    voy.show()
    # Run the main Qt loop
    sys.exit(app.exec_())

    # bonus => faire pour avoir des dates lisibles