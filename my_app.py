from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
       QApplication, QWidget,
       QHBoxLayout, QVBoxLayout,
       QGroupBox, QRadioButton,
       QPushButton, QLabel, QListWidget, QLineEdit)

from instr import *
from TestWin import *

class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.init.UI()
        self.connects()
        self.show()

    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

    def initUI(self):
        self.hello_text = QLabel( txt_hello )
        self.instruction = QLabel( txt_instructior )
        self.bullon = QPushButton( txt_next )
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.hello_text) 
        self.layout.addWidget(self.instruction) 
        self.layout.addWidget(self.button) 

    def connects(self):
        self.bnt_next.clicked.connect( self.next_click )

    def next_click(self):
        self.hide
        self.tw = TestWin()

app = QApplication([])
mw = MainWin()
app.exec_()



