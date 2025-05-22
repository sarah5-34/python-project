# final_win.py

from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout
from instr import *

class FinalWin(QWidget):
    def _init_(self, exp):
        super()._init_()
        self.exp = exp
        self.set_appear()
        self.initUI()
        self.show()

    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

    def initUI(self):
        self.index = self.results()
        self.index_text = QLabel(txt_index + str(round(self.index, 1)))
        self.work_text = QLabel(txt_workheart + self.get_performance())
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.index_text)
        self.layout.addWidget(self.work_text)
        self.setLayout(self.layout)

    def results(self):
        return (4 * (self.exp.t1 + self.exp.t2 + self.exp.t3) - 200) / 10

    def get_performance(self):
        index = self.index
        age = self.exp.age
        if age >= 15:
            if index >= 15:
                return txt_res1
            elif 11 <= index < 15:
                return txt_res2
            elif 6 <= index < 11:
                return txt_res3
            elif 0.5 <= index < 6:
                return txt_res4
            else:
                return txt_res5
        else:
            return txt_res3  # Default for under 15