import sys
from fenetre import *
from intro import *


""""##########Fonctions ############

def quitapp():
    app.quit()

################################"""

app = QApplication(sys.argv)

window = TabWidgetWindow()
window.show()

#windows2 = FirstWindow("bon","tim",19)
#windows2.show()

#window3 = MainWindow()
#window3.show("2","nom","prenom","15")



sys.exit(app.exec())
