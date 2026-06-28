import json
from PyQt5.QtWidgets import *

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.v_main_lay = QVBoxLayout()

        self.edit_t_n = QLineEdit()
        self.edit_t_n.setPlaceholderText("task name")

        self.edit_status = QLineEdit()
        self.edit_status.setPlaceholderText("status  done/pending")

        self.edit_search = QLineEdit()
        self.edit_search.setPlaceholderText("qidiruv")

        self.btn_add = QPushButton("qoshish")
        self.btn_add.clicked.connect(self.Add)

        self.btn__search = QPushButton("qidirish")
        self.btn__search.clicked.connect(self.Search)

        self.btn_total = QPushButton("umumiy son")
        self.btn_total.clicked.connect(self.Total)

        self.lbl_info = QLabel()

        self.v_main_lay.addWidget(self.edit_t_n)
        self.v_main_lay.addWidget(self.edit_status)
        self.v_main_lay.addWidget(self.edit_search)

        self.v_main_lay.addWidget(self.btn_add)
        self.v_main_lay.addWidget(self.btn__search)
        self.v_main_lay.addWidget(self.btn_total)

        self.v_main_lay.addWidget(self.lbl_info)

        self.setLayout(self.v_main_lay)

    def Add(self):
        task = self.edit_t_n.text()
        status = self.edit_status.text()

        if not task or not status:
            QMessageBox.warning(self,"xato", "Barcha maydonlarni toldiring!")
            return
        
        if status not in ["Done", "Pending"]:
            QMessageBox.critical(self,"status", "Notogri status!")
            return

        if len(task) < 3:
            QMessageBox.warning(self, "xato", "Task juda qisqa")
            return
        
        try:
            f = open("tasks.json", "r+")
            dct = json.load(f)
        except:
            dct = []
            f = open("tasks.json", "w+")

        dct.append({
            "task": task,
            "status": status
        })

        f.seek(0)
        json.dump(dct, f, indent = 4)
        QMessageBox.information(self,"message", "Task qoshildi")

        self.edit_t_n.clear()
        self.edit_status.clear()

        f.close()

    def Search(self):
        search = self.edit_search.text()

        f = open("tasks.json", "r")
        dct = json.load(f)

        for item in dct:
            if item["task"] == search:
                QMessageBox.information(self,"topildi", f'{item["task"]} - {item["status"]}')
                f.close()
                return

        QMessageBox.warning(self,"natija", "Topilmadi!")
        f.close()

    def Total(self):
        f = open("tasks.json","r")
        dct = json.load(f)

        self.lbl_info.setText("Jami tasklar:" + str(len(dct)))

        f.close()