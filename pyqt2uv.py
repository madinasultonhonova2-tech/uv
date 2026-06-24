from PyQt5.QtWidgets import *

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.v_main_lay = QVBoxLayout()
        self.h_rd_lay = QHBoxLayout()
        self.h_btn_lay = QHBoxLayout()

        self.edit_name = QLineEdit()
        self.edit_name.setPlaceholderText("name")

        self.edit_second = QLineEdit()
        self.edit_second.setPlaceholderText("second")

        self.edit_age = QLineEdit()
        self.edit_age.setPlaceholderText("age")

        self.female = QRadioButton("F")
        self.female.setStyleSheet("font-size: 20px")

        self.male = QRadioButton("M")
        self.male.setStyleSheet("font-size: 20px")

        self.shahar = QComboBox()
        self.shahar.addItems(["Tashkent", "Samarqand", "Namangan"])
        self.shahar.currentTextChanged.connect(self.Tuman)

        self.tuman = QComboBox()
        self.Tuman()

        self.btn_sub = QPushButton("submit")
        self.btn_sub.clicked.connect(self.submit)

        self.btn_exit = QPushButton("exit")
        self.btn_exit.clicked.connect(exit)

        self.h_rd_lay.addWidget(self.female)
        self.h_rd_lay.addWidget(self.male)

        self.v_main_lay.addWidget(self.edit_name)
        self.v_main_lay.addWidget(self.edit_second)
        self.v_main_lay.addWidget(self.edit_age)

        self.h_btn_lay.addWidget(self.btn_sub)
        self.h_btn_lay.addWidget(self.btn_exit)

        self.v_main_lay.addLayout(self.h_rd_lay)

        self.v_main_lay.addWidget(self.shahar)
        self.v_main_lay.addWidget(self.tuman)

        self.v_main_lay.addLayout(self.h_btn_lay)

        self.setLayout(self.v_main_lay)

    def Tuman(self):
        self.tuman.clear()
        
        if self.shahar.currentText() == "Tashkent":
            self.tuman.addItems(["Chilonzor","Yunusobod","Olmazor"])
        
        elif self.shahar.currentText() == "Samarqand":
            self.tuman.addItems(["Registon", "Siyob", "Urgut"])
                
        elif self.shahar.currentText() == "Namangan":
            self.tuman.addItems(["Chortoq", "Kosonsoy", "Pop"])

    def submit(self):
        name = self.edit_name.text()
        second = self.edit_second.text()
        age = self.edit_age.text()

        gender = ""
        if self.male.isChecked():
            gender = "Male"
        elif self.female.isChecked():
            gender = "Female"

        city = self.shahar.currentText()
        district = self.tuman.currentText()

        QMessageBox.information(
            self,
            "Info",
            f"Name: {name}\n"
            f"Second: {second}\n"
            f"Age: {age}\n"
            f"Gender: {gender}\n"
            f"City: {city}\n"
            f"District: {district}"
        )

app = QApplication([])
win = MyWindow()
win.show()
app.exec_()