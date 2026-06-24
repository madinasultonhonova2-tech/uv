
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QLineEdit

app = QApplication([])

class Calculator(QWidget):
    def __init__(self):
        super().__init__()

        layout = QGridLayout()

        self.edit = QLineEdit()
        layout.addWidget(self.edit, 0, 0, 1, 4)

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', 'C', '=', '+'
        ]

        row = 1
        col = 0

        for text in buttons:
            btn = QPushButton(text)
            btn.clicked.connect(self.on_click)
            layout.addWidget(btn, row, col)

            col += 1
            if col == 4:
                col = 0
                row += 1

        self.setLayout(layout)

    def on_click(self):
        text = self.sender().text()

        if text == "=":
            try:
                result = str(eval(self.edit.text()))
                self.edit.setText(result)
            except:
                self.edit.setText("Xato")
        elif text == "C":
            self.edit.clear()
        else:
            self.edit.setText(self.edit.text() + text)

win = Calculator()
win.show()
app.exec_()