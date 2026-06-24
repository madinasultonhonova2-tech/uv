from PyQt5.QtWidgets import *
from my_window import MyWindow

app = QApplication([])
win = MyWindow()

win.setFixedSize(500,300)

win.show()
app.exec_()