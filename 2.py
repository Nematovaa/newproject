import os
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys
os.system("cls")


class filedialog(QMainWindow):
    check=False

    def __init__(self):
        super().__init__()
        self.setMaximumSize(1240, 720)
        self.setMinimumSize(1240, 720)
        self.setWindowTitle("FileDialog bilan ishlash")
        
        self.setFont(QFont("Consolas",18))
        self.btn=QPushButton(self)
        self.btn.setGeometry(10, 10, 580, 50)
        self.btn.setText("Rasmni yuklash")
        self.btn.setStyleSheet("""
            color: rgb(0,255,0);
            background-color: rgb(0,0,0);
            border-radius: 15px;
            border-style: solid;
            border-color: rgb(0,255,0);
            border-width: 4px;
                               """)
        self.btn.clicked.connect(self.f_dialog1)
        
        self.lb = QLabel(self)
        self.lb.setGeometry(5,65,610,650)
        
        self.btn1 = QPushButton(self)
        self.btn1.setGeometry(630,10,580,50)
        self.btn1.setText("Textni yuklash")
        self.btn1.setStyleSheet("""
            color: rgb(0,255,0);
            background-color: rgb(0,0,0);
            border-radius: 15px;
            border-style: solid;
            border-color: rgb(0,255,0);
            border-width: 4px;
                               """)
        self.btn1.clicked.connect(self.f_dialog2)

        self.txt=QTextEdit(self)
        self.txt.setGeometry(625,65,610,650)
        self.txt.setStyleSheet("""
            color: rgb(0,0,200);
            background-color: rgb(55,255,175);
            border-radius: 15px;
            border-style: solid;
            border-color: rgb(0,255,0);
            border-width: 4px;
                               """)
        self.txt.setFont(QFont("Times New Roman",18))

    def f_dialog1(self):
        path=QFileDialog.getOpenFileName(self,"Rasm tanlash uchun","D:","Rasm formatlar *.jpg")[0]
        if path:
            self.lb.setPixmap(QPixmap(path))

    def f_dialog2(self):
        path=QFileDialog.getOpenFileName(self,"Rasm tanlash uchun","D:","Rasm formatlar *.txt")[0]
        if path:
            with open(path,"r") as f:
                self.txt.setText(f.read())


def main():
    app = QApplication(sys.argv)
    project = filedialog()
    project.show()
    sys.exit(app.exec_())


main()
        