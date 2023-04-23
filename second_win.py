from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
       QApplication, QWidget,
       QHBoxLayout, QVBoxLayout,
       QGroupBox, QRadioButton,
       QPushButton, QLabel, QListWidget, QLineEdit)


from instr import *
from final_win import *


line_name = QLineEdit('')

class TestWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()
    
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

    def initUI(self):
        self.r_line = QVBoxLayout()
        self.l_line = QVBoxLayout()
        self.h_line = QVBoxLayout()
        self.h_line.addWidget(self.btn1)
        self.h_line.addWidget(self.timer)
        self.h_line.addLayout(self.l_line)
        self.h_line.addLayout(self.r_line)
        self.setLayout(self.h_line)

    def next_click(self):
       self.tw = FinalWin()
       self.hide()


   def connects(self):
       self.btn_next.clicked.connect(self.next_click)