from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from os import system
import sys
system("cls")


class dastur(QMainWindow):
    check = False
    def __init__(self):
        super().__init__()
        self.setGeometry(50, 50, 1200, 780)

        self.setWindowTitle("birinchi dastur")

        self.setStyleSheet("background-color: rgb(0, 254, 195);")

        btn = QPushButton(self)
        btn.setText("Click")
        btn.setGeometry(850, 710, 275, 50)
        btn.setStyleSheet("color: lime; background-color: black;")
        btn.setFont(QFont("Consolas", 18))
        btn.clicked.connect(self.ishla)

    def ishla(self):
        if dastur.check == False:
            self.setStyleSheet("background-color: red")
            dastur.check = True
        else:
            self.setStyleSheet("background-color: black")
            dastur.check == False


app = QApplication(sys.argv)
project = dastur()
project.show()
sys.exit(app.exec_())