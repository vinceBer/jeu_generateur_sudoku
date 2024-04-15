from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from fenetre import *

class TabWidgetWindow(QTabWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.setWindowTitle("Sudoku")
        self.setMinimumSize(550,250)

        self.regles()
        self.labelConsignes()

        self.tab1 = QWidget()
        self.tab2 = QWidget()

        self.addTab(self.tab1, "Tab 1")
        self.addTab(self.tab2, "Tab 2")

        self.tab1Affiche()
        self.tab2Affiche()

    def tab1Affiche(self):
        layout = QFormLayout()
        grille = QGridLayout()

        self.prenom = QLineEdit()
        #prenom.setValidator()
        self.nom =QLineEdit()

        self.age = QLineEdit()
        self.age.setValidator(QIntValidator())
        self.age.setMaxLength(2)

        label = QLabel()
        label.setText(self.labelConsignes)

        boutonSuivant =QPushButton()
        boutonSuivant.setText("SUIVANT")
        boutonSuivant.setStyleSheet("background : grey")
        #boutonSuivant.setFixedHeight(20)
        #boutonSuivant.setFixedWidth(60)
        boutonSuivant.setFixedSize(100,20)
        boutonSuivant.clicked.connect(self.assignSuivant)

        layout.addRow("Prenom", self.prenom)
        layout.addRow("Nom", self.nom)
        layout.addRow("Age", self.age)
        layout.addWidget(label)
        layout.addWidget(boutonSuivant)
        layout.setAlignment(Qt.AlignCenter)

        self.setTabText(0, "Inscription")
        self.tab1.setLayout(layout)

    def tab2Affiche(self):
        texte = self.lesRegles
        texteEdit = QTextEdit()
        texteEdit.setText(texte)
        texteEdit.setEnabled(False)
        texteEdit.setStyleSheet("font:10px;color:black;background-color:white")

        layout = QFormLayout()
        joue = QHBoxLayout()
        joue.addWidget(QRadioButton("Oui"))
        joue.addWidget(QRadioButton("Non"))
        joue.addWidget(texteEdit)
        layout.addRow(QLabel("Avez vous déja joué au Sudoku ?"), joue)

        self.setTabText(1, "Consignes")
        self.tab2.setLayout(layout)

    def assignSuivant(self):
        if self.prenom.text() != "" and self.nom.text() != "" and self.age.text() != "":
            print("tous les champs sont complétés")
            print(self.prenom.text(), self.nom.text(), self.age.text())
            self.window = FirstWindow(self.nom.text(), self.prenom.text(), self.age.text())
            self.window.show()
            self.close()
        else :
            print("pas encore complété")

    def regles(self):
        self.lesRegles ="""Le Sudoku est un jeu dans lequel il faut réussir à mettre
une valeur de 1 à 9 dans chaune des case et sur chaque lignes. 
Il ne doit pas y avoir 2 fois la même valeur sur une ligne ou une colone"""

    def labelConsignes(self):
        self.labelConsignes ="""Vous pouvez jouer directement, après avoir rentré vos données
dans les case vide ci-dessus en appuyant sur "SUIVANT"
ou lire les règles du Sudoku dans l'onglet "Consignes" situé en haut de la page"""
