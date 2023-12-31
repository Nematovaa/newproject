import random
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    num = 1
    count = 0

    def setupUi(self, MainWindow):
        MainWindow.setWindowTitle("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        MainWindow.setStyleSheet("background-color: rgb(255, 222, 184);")
        MainWindow.setAnimated(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.omad = QtWidgets.QRadioButton(self.centralwidget)
        self.omad.setGeometry(QtCore.QRect(20, 20, 95, 20))
        self.omad.setObjectName("radioButton")
        self.omad.clicked.connect(lambda: self.radioBtn(self.omad))
        self.sharqona = QtWidgets.QRadioButton(self.centralwidget)
        self.sharqona.setGeometry(QtCore.QRect(130, 20, 121, 20))
        self.sharqona.setObjectName("radioButton_2")
        self.sharqona.clicked.connect(lambda: self.radioBtn(self.sharqona))
        self.super = QtWidgets.QRadioButton(self.centralwidget)
        self.super.setGeometry(QtCore.QRect(270, 20, 95, 20))
        self.super.setObjectName("radioButton_3")
        self.super.clicked.connect(lambda: self.radioBtn(self.super))
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(20, 60, 281, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.textEdit.setFont(font)
        self.textEdit.setAcceptDrops(True)
        self.textEdit.setStyleSheet("border-width:3px;\n"
                                    "border-style:solid;\n"
                                    "border-radius:15%;\n"
                                    "border-color: rgb(52, 16, 255);\n"
                                    "background-color:white;\n"
                                    "")
        self.textEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setReadOnly(True)

        self.init_nums(MainWindow)

        self.pushButton_37 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_37.setGeometry(QtCore.QRect(310, 60, 61, 41))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_37.setFont(font)
        self.pushButton_37.setStyleSheet("border-width:3px;\n"
                                         "border-style:solid;\n"
                                         "border-color:red;\n"
                                         "background-color: rgb(177, 177, 177);\n"
                                         "border-radius:15%;")
        self.pushButton_37.setObjectName("pushButton_37")
        self.pushButton_37.clicked.connect(self.addVariant)

        self.start = QtWidgets.QPushButton(self.centralwidget)
        self.start.setGeometry(QtCore.QRect(420, 10, 71, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.start.setFont(font)
        self.start.setToolTipDuration(4)
        self.start.setStyleSheet("border-width:3px;\n"
                                 "border-style:solid;\n"
                                 "border-color: rgb(165, 44, 44);\n"
                                 "background-color: rgb(177, 177, 177);\n"
                                 "border-radius:10%;")
        self.start.setObjectName("pushButton_38")
        self.start.clicked.connect(self.start_connect)

        self.pushButton_39 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_39.setGeometry(QtCore.QRect(500, 10, 31, 31))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)

        self.resultList = list()

        self.pushButton_39.setFont(font)
        self.pushButton_39.setStyleSheet("border-width:3px;\n"
                                         "border-style:solid;\n"
                                         "border-color:black;\n"
                                         "background-color:orange;\n"
                                         "border-radius:15px")
        self.pushButton_39.setText("")
        self.pushButton_39.setObjectName("pushButton_39")
        self.resultList.append(self.pushButton_39)
        self.pushButton_40 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_40.setGeometry(QtCore.QRect(540, 10, 31, 31))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_40.setFont(font)
        self.pushButton_40.setStyleSheet("border-width:3px;\n"
                                         "border-style:solid;\n"
                                         "border-color:black;\n"
                                         "background-color:orange;\n"
                                         "border-radius:15px")
        self.pushButton_40.setText("")
        self.pushButton_40.setObjectName("pushButton_40")
        self.pushButton_41 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_41.setGeometry(QtCore.QRect(580, 10, 31, 31))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_41.setFont(font)
        self.pushButton_41.setStyleSheet("border-width:3px;\n"
                                         "border-style:solid;\n"
                                         "border-color:black;\n"
                                         "background-color:orange;\n"
                                         "border-radius:15px")
        self.pushButton_41.setText("")
        self.pushButton_41.setObjectName("pushButton_41")
        self.pushButton_42 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_42.setGeometry(QtCore.QRect(620, 10, 31, 31))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_42.setFont(font)
        self.pushButton_42.setStyleSheet("border-width:3px;\n"
                                         "border-style:solid;\n"
                                         "border-color:black;\n"
                                         "background-color:orange;\n"
                                         "border-radius:15px")
        self.pushButton_42.setText("")
        self.pushButton_42.setObjectName("pushButton_42")
        self.pushButton_43 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_43.setGeometry(QtCore.QRect(660, 10, 31, 31))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_43.setFont(font)
        self.pushButton_43.setStyleSheet("border-width:3px;\n"
                                         "border-style:solid;\n"
                                         "border-color:black;\n"
                                         "background-color:orange;\n"
                                         "border-radius:15px")
        self.pushButton_43.setText("")
        self.pushButton_43.setObjectName("pushButton_43")
        self.pushButton_44 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_44.setGeometry(QtCore.QRect(700, 10, 31, 31))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_44.setFont(font)
        self.pushButton_44.setStyleSheet("border-width:3px;\n"
                                         "border-style:solid;\n"
                                         "border-color:black;\n"
                                         "background-color:orange;\n"
                                         "border-radius:15px")
        self.pushButton_44.setText("")
        self.pushButton_44.setObjectName("pushButton_44")
        self.pushButton_45 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_45.setGeometry(QtCore.QRect(740, 10, 31, 31))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_45.setFont(font)
        self.pushButton_45.setStyleSheet("border-width:3px;\n"
                                         "border-style:solid;\n"
                                         "border-color:black;\n"
                                         "background-color:orange;\n"
                                         "border-radius:15px")
        self.pushButton_45.setText("")
        self.pushButton_45.setObjectName("pushButton_45")
        self.resultList.append(self.pushButton_40)
        self.resultList.append(self.pushButton_41)
        self.resultList.append(self.pushButton_42)
        self.resultList.append(self.pushButton_43)
        self.resultList.append(self.pushButton_44)
        self.resultList.append(self.pushButton_45)
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(423, 56, 361, 381))
        self.textEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                      "border-width:3px;\n"
                                      "border-color:black;\n"
                                      "border-style:solid;\n"
                                      "border-radius:10%")
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_2.setReadOnly(True)
        self.pushButton_46 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_46.setGeometry(QtCore.QRect(20, 490, 171, 28))
        self.pushButton_46.setStyleSheet("color:  rgb(0, 66, 198);\n"
                                         "background-color: rgb(78, 235, 235);\n"
                                         "border-width:3px;\n"
                                         "border-style:solid;\n"
                                         "border-radius:14%;\n"
                                         "border-color: rgb(0, 66, 198);")
        self.pushButton_46.setObjectName("pushButton_46")
        self.pushButton_47 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_47.setGeometry(QtCore.QRect(210, 490, 171, 28))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_47.setFont(font)
        self.pushButton_47.setStyleSheet("color:  rgb(0, 66, 198);\n"
                                         "background-color: rgb(0, 213, 213);\n"
                                         "border-width:3px;\n"
                                         "border-style:solid;\n"
                                         "border-radius:14%;\n"
                                         "border-color: rgb(0, 66, 198);")
        self.pushButton_47.setObjectName("pushButton_47")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.numbers = list()
        self.variants = list()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.omad.setText(_translate("MainWindow", "Omad(36/5)"))
        self.sharqona.setText(_translate("MainWindow", "Sharqona(36/6)"))
        self.super.setText(_translate("MainWindow", "Super(36/7)"))
        self.pushButton_37.setText(_translate("MainWindow", "+"))
        self.start.setText(_translate("MainWindow", "Start"))
        self.pushButton_46.setText(_translate("MainWindow", "Telegramm"))
        self.pushButton_47.setText(_translate("MainWindow", "YOU TUBE"))

    def init_nums(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        y = 120
        for i in range(6):
            x = 20
            for j in range(6):
                pushButton = QtWidgets.QPushButton(self.centralwidget)
                pushButton.setGeometry(QtCore.QRect(x, y, 50, 50))
                font = QtGui.QFont()
                font.setFamily("MS Reference Sans Serif")
                font.setPointSize(16)
                font.setBold(False)
                font.setWeight(50)
                pushButton.setFont(font)
                pushButton.setStyleSheet("border-width:3px;\n"
                                         "border-style:solid;\n"
                                         "border-color: rgb(156, 71, 71);\n"
                                         "background-color: rgb(240, 209, 219);\n"
                                         "border-radius:25px")
                pushButton.setObjectName("pushButton")
                pushButton.clicked.connect(self.clikcBtn)
                pushButton.setText(_translate("MainWindow", str(Ui_MainWindow.num)))
                Ui_MainWindow.num += 1
                x += 60
            y += 60
    def start_connect(self):
        if len(self.variants) > 0:
            randList = list()
            for i in range(Ui_MainWindow.count):
                r = str(random.randint(1, 36))
                randList.append(r)
                self.resultList[i].setText(r)

            for i in self.variants:
                c = 0
                for j in i:
                    if j in randList:
                        c += 1
                print(f"{i} -> {c} ta mos keldi")

            self.textEdit.clear()
            self.textEdit_2.clear()
            self.numbers.clear()
            self.variants.clear()

    def button(self, add_button=None):
        i = 420
        j = 60
        if self.start_connect:
            for x in self.variants:
                for y in self.variants:
                    add_button.QPushButton(self.variants[x][y],self)
                    add_button.setGeometry(i,j,50,50)
                    j += 60
                i += 60

    def radioBtn(self, radio):
        if radio.isChecked():
            self.numbers.clear()
            self.textEdit.clear()
            self.textEdit_2.clear()
            self.variants.clear()
            if self.omad.isChecked():
                Ui_MainWindow.count = 5
            elif self.sharqona.isChecked():
                Ui_MainWindow.count = 6
            elif self.super.isChecked():
                Ui_MainWindow.count = 7
            else:
                Ui_MainWindow.count = -1

    def clikcBtn(self):
        if Ui_MainWindow.count > len(self.numbers):
            d = self.centralwidget.sender().text()
            if d not in self.numbers:
                self.numbers.append(d)
                self.textEdit.setText(", ".join(self.numbers))

    def addVariant(self):
        if Ui_MainWindow.count == len(self.numbers):
            self.variants.append(self.numbers.copy())
            allVariants = str()
            for i in self.variants:
                allVariants = allVariants + ", ".join(i) + "\n"

            self.textEdit_2.setText(allVariants)
            self.numbers.clear()
            self.textEdit.clear()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
