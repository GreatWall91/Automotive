#Grafiche
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
import random

Titolidisponibili = [x for x in range(10)]

class _MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Ricette")

        self.button = QPushButton("Aggiungi")

        self.button.clicked.connect(self.thebutton)
        self.windowTitleChanged.connect(self.changedtitle)

        self.setCentralWidget(self.button)

    def thebutton(self, ciao):        
        self.setWindowTitle(f"{random.choice(Titolidisponibili)}")

    def changedtitle(self, title__):
        print(title__)
        if title__ == "5":
            self.button.setEnabled(False)
            self.button.setText("porcodio")





#Classe di tutti gli step tranne quello di base.
class NewStep:
    StepNumber = 0
    IsScrewStep = False
    Steps = [False for x in range(5)]
    IsNecessary = [False for x in range(5)]
    Wait = 0
    Text = ""
    def WriteNewStep(self, FilePath):

        #File aperto in modalità append
        FileOpen = open(FilePath, "a")
        StringToWrite = "["

        #Aggiunge la S se si tratta di uno step di avvitatura
        if self.IsScrewStep:
            StringToWrite = StringToWrite + "S"
        
        #Scrive il numero dello step
        StringToWrite = StringToWrite + f"{self.StepNumber}]\n"
        x = 0

        #Ciclo for per scrivere le varie uscite necessarie
        for x in range(5):
            if self.IsNecessary[x]:
                StringToWrite = StringToWrite + f"{x + 1}= "
                if self.Steps[x]:
                    StringToWrite = StringToWrite + "true\n"
                else:
                    StringToWrite = StringToWrite + "false\n"
        
        #Scrive la variabile dell'istruzione
        if self.Text != "":
            StringToWrite = StringToWrite + f"text= {self.Text}\n"
        
        #Scrive il tempo di attesa
        if self.Wait != 0:
            StringToWrite = StringToWrite + f"wait= {self.Wait}\n"
        
        #Aggiunge lo spazio tra uno step e l'altro
        StringToWrite = StringToWrite + "\n"

        #Scrive su file e chiude
        FileOpen.write(StringToWrite)
        FileOpen.close     

#Creazione dell'applicazione con argomento che sarebbe la lista dei comandi per l'applicazione.
#Andava bene anche scritta come argomento ([])
MainApp = QApplication(sys.argv)

#Finestra principale abilitata a essere vista.
#Tutto è un widget, in questo caso la finestra.
#MainWindow = QWidget()
MainWindow = _MainWindow()
MainWindow.show()

MainApp.exec_()


