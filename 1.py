import os
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys
os.system("cls")
class cdialog(QMainWindow):
    check=False
    def __init__(self):
        super().__init__()
        self.setMaximumSize(640,480)
        self.setMinimumSize(640,480)
        self.setWindowTitle("Color dialog bilan ishlash")
        
        self.lb=QLabel("Tanlang: ",self)
        self.btn=QPushButton("Change Font",self)
        self.txt=QLineEdit(self)
        self.cmb=QComboBox(self)
        
        self.lb.setGeometry(75,100,250,50)
        self.cmb.setGeometry(75,160,250,50)
        self.cmb.addItems(["Label","Button","LineEdit"])
        
        self.rdb1=QRadioButton("Color",self)
        self.rdb2=QRadioButton("Background-color",self)
        self.rdb1.setGeometry(100,220,250,50)
        self.rdb2.setGeometry(100,275,250,50)
        
        self.txt.setGeometry(380,150,250,50)
        self.btn.setGeometry(380,220,250,50)
        self.btn.clicked.connect(self.fnt_dialog)
    def fnt_dialog(self):
        if cdialog.check==False:
            temp,ok=QFontDialog.getFont()
            if ok:
                self.setFont(QFont(temp))
            else:
                print("Siz fontni tanlamadingiz")
            cdialog.check=True
        else:
            cdialog.check=False
            color=QColorDialog.getColor()
            if color:
                if self.rdb1.isChecked()==True:
                    match self.cmb.currentText():
                        case "Label":
                            self.lb.setStyleSheet(f"color: {color.name()}")
                        case "Button":
                            self.btn.setStyleSheet(f"color: {color.name()}")
                        case "LineEdit":
                            self.txt.setStyleSheet(f"color: {color.name()}")
                else:
                    match self.cmb.currentText():
                        case "Label":
                            self.lb.setStyleSheet(f"background-color: {color.name()}")
                        case "Button":
                            self.btn.setStyleSheet(f"background-color: {color.name()}")
                        case "LineEdit":
                            self.txt.setStyleSheet(f"background-color: {color.name()}")
            else:
                print("Siz rang tanlamadingiz")
                
            
            

def main():
    app=QApplication(sys.argv)
    project=cdialog()
    project.show()
    sys.exit(app.exec_())

main()