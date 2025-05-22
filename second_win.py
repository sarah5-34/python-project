# second_win.py

from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
from PyQt5.QtCore import Qt, QTimer, QTime
from PyQt5.QtGui import QFont
from instr import *
from final_win import FinalWin

class Experiment:
    def _init_(self, age, t1, t2, t3):
        self.age = int(age)
        self.t1 = int(t1)
        self.t2 = int(t2)
        self.t3 = int(t3)

class TestWin(QWidget):
    def _init_(self):
        super()._init_()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()

    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

    def initUI(self):
        self.name_label = QLabel('Enter your full name:')
        self.name_input = QLineEdit('Full Name')
        self.age_label = QLabel('Enter your age:')
        self.age_input = QLineEdit('0')
        self.test1_label = QLabel('Heart rate before test:')
        self.test1_input = QLineEdit('0')
        self.test2_label = QLabel('Heart rate after squats:')
        self.test2_input = QLineEdit('0')
        self.test3_label = QLabel('Heart rate after rest:')
        self.test3_input = QLineEdit('0')

        self.text_timer = QLabel('00:00:00')
        self.text_timer.setFont(QFont('Times', 36, QFont.Bold))

        self.test1_button = QPushButton('Start first test')
        self.test2_button = QPushButton('Start squats')
        self.test3_button = QPushButton('Start final test')

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.name_label)
        self.layout.addWidget(self.name_input)
        self.layout.addWidget(self.age_label)
        self.layout.addWidget(self.age_input)
        self.layout.addWidget(self.text_timer)
        self.layout.addWidget(self.test1_label)
        self.layout.addWidget(self.test1_input)
        self.layout.addWidget(self.test1_button)
        self.layout.addWidget(self.test2_button)
        self.layout.addWidget(self.test2_label)
        self.layout.addWidget(self.test2_input)
        self.layout.addWidget(self.test3_button)
        self.layout.addWidget(self.test3_label)
        self.layout.addWidget(self.test3_input)
        self.setLayout(self.layout)

    def connects(self):
        self.test1_button.clicked.connect(self.timer_test)
        self.test2_button.clicked.connect(self.timer_squats)
        self.test3_button.clicked.connect(self.timer_final)
        self.test3_button.clicked.connect(self.next_click)

    def timer_test(self):
        self.time = QTime(0, 0, 15)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer1Event)
        self.timer.start(1000)

    def timer1Event(self):
        self.time = self.time.addSecs(-1)
        self.text_timer.setText(self.time.toString('hh:mm:ss'))
        self.text_timer.setStyleSheet('color: green')
        if self.time == QTime(0, 0, 0):
            self.timer.stop()

    def timer_squats(self):
        self.time = QTime(0, 0, 45)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer2Event)
        self.timer.start(1000)

    def timer2Event(self):
        self.time = self.time.addSecs(-1)
        self.text_timer.setText(self.time.toString('hh:mm:ss'))
        self.text_timer.setStyleSheet('color: black')
        if self.time == QTime(0, 0, 0):
            self.timer.stop()

    def timer_final(self):
        self.time = QTime(0, 1, 0)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer3Event)
        self.timer.start(1000)

    def timer3Event(self):
        self.time = self.time.addSecs(-1)
        self.text_timer.setText(self.time.toString('hh:mm:ss'))
        secs = self.time.second()
        if secs > 45:
            self.text_timer.setStyleSheet('color: green')
        elif 15 < secs <= 45:
            self.text_timer.setStyleSheet('color: black')
        else:
            self.text_timer.setStyleSheet('color: green')
        if self.time == QTime(0, 0, 0):
            self.timer.stop()

    def next_click(self):
        try:
            self.hide()
            self.exp = Experiment(self.age_input.text(), self.test1_input.text(),
                                  self.test2_input.text(), self.test3_input.text())
            self.fw = FinalWin(self.exp)
        except ValueError:
            self.age_input.setText('0')
            self.test1_input.setText('0')
            self.test2_input.setText('0')
            self.test3_input.setText('0')