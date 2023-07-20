import os
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
os.system("cls")

class Omad_lotto(QMainWindow):
    count=0
    def __init__(self):
        super().__init__()
        self.setFont(QFont("Consolas",18))
        self.setMaximumSize(1240,720)
        self.setMinimumSize(1240,720)
        self.setWindowTitle("MDI bilan ishlash")
        
        self.mdi=QMdiArea()
        self.setCentralWidget(self.mdi)
        
        self.bar=self.menuBar()
        
        self.menyu=self.bar.addMenu("MDI")
        self.menyu.setFont(QFont("Consolas",18))
        self.new=QAction("New",self)
        self.cascad=QAction("Caskad",self)
        self.tile=QAction("Tile",self)
        
        self.menyu.addActions([self.new,self.cascad,self.tile])
        
        self.new.triggered.connect(self.trg_new)
        self.cascad.triggered.connect(self.trg_cas)
        self.tile.triggered.connect(self.trg_til)

    def trg_new(self):
        Omad_lotto.count+=1
        oyna=QMdiSubWindow(self.mdi)
        print(self.mdi.subWindowList())
        oyna.setWidget(QTextEdit())
        oyna.setWindowTitle(f"SubWindow N{Omad_lotto.count}")
        oyna.show()
    
    def trg_cas(self):
        self.mdi.cascadeSubWindows()
    
    def trg_til(self):
        self.mdi.tileSubWindows()
        
            


def main():
    app=QApplication(sys.argv)
    project=Omad_lotto()
    project.show()
    sys.exit(app.exec_())

main()