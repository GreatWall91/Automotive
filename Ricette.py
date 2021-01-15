import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QSpinBox

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("MyApp")

        widget = QSpinBox()

        widget.setMinimum(-10)
        widget.setMaximum(10)

        widget.setPrefix("$")
        widget.setSuffix("c")

        widget.setSingleStep(3)

        widget.valueChanged.connect(self.value_changed)
        widget.valueChanged[str].connect(self.value_changed_str)

        self.setCentralWidget(widget)

    def value_changed(self, i):
        print(i)

    def value_changed_str(self, j):
        print(j)


#Classe di tutti gli step tranne quello di base.
class NewStep:
    def __init__(self):
        self.StepNumber = 0
        self.IsScrewStep = False
        self.Steps = [False for x in range(5)]
        self.IsNecessary = [False for x in range(5)]
        self.Wait = 0
        self.Text = ""
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

MainMainWindow = MainWindow()
MainMainWindow.show()

MainApp.exec_()
