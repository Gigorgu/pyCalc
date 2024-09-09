import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QLineEdit
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt, QSize

class Calculator(QWidget):
    def __init__(self):
        super().__init__()

        self.setStyleSheet("""
            QWidget {
                background-color: #121212;
                color: #e0e0e0;
                font-family: 'Arial', sans-serif;
            }
            QLineEdit {
                background-color: #1e1e1e;
                border: 1px solid #333;
                padding: 10px;
                border-radius: 8px;
                font-size: 24px;
            }
            QPushButton {
                background-color: #333;
                border: none;
                color: #e0e0e0;
                font-size: 24px;
                border-radius: 8px;
            }
            QPushButton:pressed {
                background-color: #555;
            }
            QPushButton:focus {
                outline: none;
            }
        """)

        self.setFont(QFont('Arial', 18))

        self.display = QLineEdit()
        self.display.setAlignment(Qt.AlignRight)
        self.display.setReadOnly(True)

        self.grid = QGridLayout()
        self.setLayout(self.grid)

        self.buttons = [
            ('C', 'clear'), ('7', '7'), ('8', '8'), ('9', '9'), ('/', '/'),
            ('4', '4'), ('5', '5'), ('6', '6'), ('*', '*'),
            ('1', '1'), ('2', '2'), ('3', '3'), ('-', '-'),
            ('0', '0'), ('.', '.'), ('=', '='), ('+', '+')
        ]
        
        self.create_buttons()
        self.setWindowTitle("Calculator")
        self.setGeometry(100, 100, 400, 600)
        self.show()
        
        
        
    def create_buttons(self):
        positions = [(i, j) for i in range(1, 5) for j in range(4)]
        for position, (text, value) in zip(positions, self.buttons):
            button = QPushButton(text)
            button.setFixedSize(QSize(80, 80))  
            button.clicked.connect(self.on_click)
            self.grid.addWidget(button, *position)

        self.grid.addWidget(self.display, 0, 0, 1, 4)

        self.grid.setRowStretch(0, 1) 
        for i in range(1, 5):
            self.grid.setRowStretch(i, 1) 
        for j in range(4):
            self.grid.setColumnStretch(j, 1) 

    def on_click(self):
        sender = self.sender()
        text = sender.text()
        current_text = self.display.text()

        if text == 'C':
            self.display.clear()
        elif text == '=':
            try:
                result = str(eval(current_text))
                self.display.setText(result)
            except Exception:
                self.display.setText('Error')
        else:
            new_text = current_text + text
            self.display.setText(new_text)

    def keyPressEvent(self, event):
        key = event.text()
        if key in '0123456789+-*/.':
            self.display.setText(self.display.text() + key)
        elif key == '\r':
            try:
                result = str(eval(self.display.text()))
                self.display.setText(result)
            except Exception:
                self.display.setText('Error')
        elif key == '\x08':
            self.display.setText(self.display.text()[:-1])

if __name__ == '__main__':
    app = QApplication(sys.argv)
    calc = Calculator()
    sys.exit(app.exec_())