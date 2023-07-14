from PyQt5.QtGui import *  # Qbutton
from PyQt5.QtCore import *  # QFOnt
from PyQt5.QtWidgets import *  # Qmainwindow
from os import system
import sys

system("cls")


class project(QMainWindow):
    cmb = []
    def __init__(self):
        super().__init__()
        self.setMaximumSize(640, 480)
        self.setMinimumSize(640, 480)
        self.setWindowTitle("TOPSHIRIQ")
        self.setStyleSheet("background-color: rgb(0,205,0);")
        self.btn1 = QPushButton("Second window",self)
        self.btn1.setGeometry(450,300,150,50)

        self.lb=QLabel("Ma'lumot kiriting:",self)
        self.lb.setFont(QFont("Calibri",18))
        self.lb.setGeometry(100,50,350,50)
        self.ln=QLineEdit(self)
        self.ln.setFont(QFont("Calibri", 18))
        self.ln.setGeometry(120, 105, 250, 50)
        btn=QPushButton("Add",self)
        btn.setGeometry(100,165,250,50)
        btn.setFont(QFont("Times New Roman",18))
        btn.clicked.connect(lambda x:self.qushish(self.ln.text()))
        self.btn1.clicked.connect(self.ulan)
    def ulan(self):
        self.oyna = ilova()
        self.oyna.show()
        #self.button = QLabel(self.cmb,self)

    def qushish(self,st):
        self.cmb.append(st)
        self.ln.clear()


class ilova(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setMaximumSize(600,300)
        self.setMinimumSize(600,300)
        self.setFont(QFont("Calibri",18))
        self.setStyleSheet("bacground-color: rgb(155,25,0);")
        self.lb1=QLabel(f"{project.cmb}",self)
        self.lb1.setFont(QFont("Calibri",18))
        self.lb1.setGeometry(100,50,350,50)
        '''self.btn = QPushButton("Second window",self)
        self.btn.setGeometry(305,50,250,50)
        self.btn.clicked.connect(self.ulan)
    def ulan(self):
        self.oyna = project()
        self.oyna.show'''


app = QApplication(sys.argv)
cod=project()
cod.show()
sys.exit(app.exec_())

