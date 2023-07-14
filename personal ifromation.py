import sys
from PyQt5.QtWidgets import *


class Info(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Information")
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.provinces = ["Toshkent", "Davomi bor"]
        self.districts = ["Yunusobod", "Mirzo Ulug'bek", "Shayxontohur", "Yakkasaroy", "Chilonzor"]
        self.genders = ["Erkak", "Ayol"]
        self.nationalities = ["O'zbek", "Qozoq", "Tojik", "Qirg'iz", "Turkman"]
        self.selected_province = ""
        self.selected_district = ""
        self.selected_gender = ""
        self.selected_nationality = ""
        self.create_form()

    def create_form(self):
        self.layout.addWidget(QLabel("Tug'ilgan viloyatingizni tanlang:"))
        province_combo = QComboBox()
        province_combo.addItems(self.provinces)
        province_combo.currentIndexChanged.connect(self.select_province)
        self.layout.addWidget(province_combo)

        self.layout.addWidget(QLabel("Tuman yoki shaharingizni tanlang:"))
        district_combo = QComboBox()
        district_combo.addItems(self.districts)
        district_combo.currentIndexChanged.connect(self.select_district)
        self.layout.addWidget(district_combo)

        self.layout.addWidget(QLabel("Jinsingizni tanlang:"))
        gender_combo = QComboBox()
        gender_combo.addItems(self.genders)
        gender_combo.currentIndexChanged.connect(self.select_gender)
        self.layout.addWidget(gender_combo)

        self.layout.addWidget(QLabel("Millatingizni tanlang:"))
        nationality_combo = QComboBox()
        nationality_combo.addItems(self.nationalities)
        nationality_combo.currentIndexChanged.connect(self.select_nationality)
        self.layout.addWidget(nationality_combo)

        self.layout.addWidget(QPushButton("Ma'lumotlarni ko'rish", clicked=self.show_info))

    def select_province(self, index):
        self.selected_province = self.provinces[index]

    def select_district(self, index):
        self.selected_district = self.districts[index]

    def select_gender(self, index):
        self.selected_gender = self.genders[index]

    def select_nationality(self, index):
        self.selected_nationality = self.nationalities[index]

    def show_info(self):
        info = f"Tug'ilgan viloyat: {self.selected_province}\n"
        info += f"Tuman yoki shahar: {self.selected_district}\n"
        info += f"Jins: {self.selected_gender}\n"
        info += f"Millat: {self.selected_nationality}"
        self.layout.addWidget(QLabel(info))


app = QApplication(sys.argv)
personal_info = Info()
personal_info.show()
sys.exit(app.exec_())
