from PyQt5.QtGui import *  # Qbutton qQw
from PyQt5.QtCore import *  # QFOnt
from PyQt5.QtWidgets import *  # QmainwindowU
from os import system
import sys # 
system("cls")
class dastur(QMainWindow):
    def __init__(self):
        # asosiy oynani chiqarish
        super().__init__()
        self.setMinimumSize(380, 600)
        self.setMaximumSize(380, 600)
        self.setWindowTitle("Calculator")
        self.setStyleSheet("background-color: rgb(0,0,54);")
        self.setWindowIcon(QIcon("D:\\calculator.ico"))

        # Qlineedit
        self.on = QPushButton("(", self)
        self.on.setGeometry(30, 200, 150, 60)
        self.on.setFont(QFont("Times New Roman", 20))
        self.on.setStyleSheet("""background-color: rgb(0,33,71);color: white;border-width: 1px;border-style: solid;border-radius: 30px;border-color: elephant;""")

        self.on = QPushButton(")", self)
        self.on.setGeometry(190, 200, 150, 60)
        self.on.setFont(QFont("Times New Roman", 20))
        self.on.setStyleSheet("""background-color: rgb(0,33,71);color: white;border-width: 1px;border-style: solid;border-radius: 30px;border-color: elephant""")

        self.seven = QPushButton("7", self)
        self.seven.setGeometry(30, 270, 60, 60)
        self.seven.setFont(QFont("Times New Roman", 20))
        self.seven.setStyleSheet("""background-color: white;color: black;border-width: 1px;border-style: solid;border-radius: 30px;border-color: black;""")

        self.four = QPushButton("4", self)
        self.four.setGeometry(30, 340, 60, 60)
        self.four.setFont(QFont("Times New Roman", 20))
        self.four.setStyleSheet("""background-color: white;color: black;border-width: 1px;border-style: solid;border-radius: 30px;border-color: black;""")

        self.one = QPushButton("1", self)
        self.one.setGeometry(30, 410, 60, 60)
        self.one.setFont(QFont("Times New Roman", 20))
        self.one.setStyleSheet("""background-color: white;color: black;border-width: 1px;border-style: solid;border-radius: 30px;border-color: black;""")

        self.zero = QPushButton("0", self)
        self.zero.setGeometry(30, 480, 60, 60)
        self.zero.setFont(QFont("Times New Roman", 20))
        self.zero.setStyleSheet("""background-color: white;color: black;border-width: 1px;border-style: solid;border-radius: 30px;border-color: black;""")

        self.eight = QPushButton("8", self)
        self.eight.setGeometry(100, 270, 60, 60)
        self.eight.setFont(QFont("Times New Roman", 20))
        self.eight.setStyleSheet("""background-color: white;color: black;border-width: 1px;border-style: solid;border-radius: 30px;border-color: black;""")

        self.five = QPushButton("5", self)
        self.five.setGeometry(100, 340, 60, 60)
        self.five.setFont(QFont("Times New Roman", 20))
        self.five.setStyleSheet("""background-color: white;color: black;border-width: 1px;border-style: solid;border-radius: 30px;border-color: black;""")

        self.two = QPushButton("2", self)
        self.two.setGeometry(100, 410, 60, 60)
        self.two.setFont(QFont("Times New Roman", 20))
        self.two.setStyleSheet("""background-color: white;color: black;border-width: 1px;border-style: solid;border-radius: 30px;border-color: black;""")

        self.dot = QPushButton(".", self)
        self.dot.setGeometry(100, 480, 60, 60)
        self.dot.setFont(QFont("Times New Roman", 20))
        self.dot.setStyleSheet("""background-color: white;color: black;border-width: 1px;border-style: solid;border-radius: 30px;border-color: black;""")

        self.nine = QPushButton("9", self)
        self.nine.setGeometry(170, 270, 60, 60)
        self.nine.setFont(QFont("Times New Roman", 20))
        self.nine.setStyleSheet("""background-color: white;color: black;border-width: 1px;border-style: solid;border-radius: 30px;border-color: black;""")

        self.six = QPushButton("6", self)
        self.six.setGeometry(170, 340, 60, 60)
        self.six.setFont(QFont("Times New Roman", 20))
        self.six.setStyleSheet("""background-color: white;color: black;border-width: 1px;border-style: solid;border-radius: 30px;border-color: black;""")

        self.three = QPushButton("3", self)
        self.three.setGeometry(170, 410, 60, 60)
        self.three.setFont(QFont("Times New Roman", 20))
        self.three.setStyleSheet("""background-color: white;color: black;border-width: 1px;border-style: solid;border-radius: 30px;border-color: black;""")

        self.C = QPushButton("C", self)
        self.C.setGeometry(170, 480, 60, 60)
        self.C.setFont(QFont("Times New Roman", 20))
        self.C.setStyleSheet("""background-color: white;color: black;border-width: 1px;border-style: solid;border-radius: 30px;border-color: black;""")

        self.minus = QPushButton("-", self)
        self.minus.setGeometry(240, 270, 60, 60)
        self.minus.setFont(QFont("Times New Roman", 20))
        self.minus.setStyleSheet("""background-color: rgb(0,0,96);color: white;border-width: 1px;border-style: solid;border-radius: 30px;border-color: black;""")

        self.division = QPushButton("/", self)
        self.division.setGeometry(310, 270, 60, 60)
        self.division.setFont(QFont("Times New Roman", 20))
        self.division.setStyleSheet("""background-color: rgb(0,0,96);color: white;border-width: 1px;border-style: solid;border-radius: 30px;border-color: black;""")

        self.multiplication = QPushButton("*", self)
        self.multiplication.setGeometry(310, 340, 60, 60)
        self.multiplication.setFont(QFont("Times New Roman", 20))
        self.multiplication.setStyleSheet("""background-color: rgb(0,0,96);color: white;border-width: 1px;border-style: solid;border-radius: 30px;border-color: black;""")

        self.plus = QPushButton("+", self)
        self.plus.setGeometry(240, 340, 60, 130)
        self.plus.setFont(QFont("Times New Roman", 20))
        self.plus.setStyleSheet("""background-color: rgb(0,0,96);color: white;border-width: 1px;border-style: solid;border-radius: 30px;border-color: black;""")

        self.division2 = QPushButton("%", self)
        self.division2.setGeometry(310, 410, 60, 60)
        self.division2.setFont(QFont("Times New Roman", 20))
        self.division2.setStyleSheet("""background-color: rgb(0,0,96);color: white;border-width: 1px;border-style: solid;border-radius: 30px;border-color: black;""")

        self.equal = QPushButton("=", self)
        self.equal.setGeometry(240, 480, 130, 60)
        self.equal.setFont(QFont("Times New Roman", 20))
        self.equal.setStyleSheet("""background-color: rgb(0,0,96);color: white;border-width: 1px;border-style: solid;border-radius: 30px;border-color: black;""")


app = QApplication(sys.argv)
project = dastur()
project.show()
sys.exit(app.exec_())
