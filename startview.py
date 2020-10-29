from PyQt5.QtWidgets import QMainWindow, QPushButton, QGridLayout, QApplication, QWidget
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtCore import QDate, Qt
import sys
from tkinter import *


class picture(QMainWindow):

    def __init__(self):
        super().__init__()
        self.date = QDate.currentDate()
        self.initUI()

    def initUI(self):
        btn1 = QPushButton('&시작', self)  # 해당 버튼에 보여질 글자
        btn2 = QPushButton('종료', self)

        w1 = QWidget(self)
        grid = QGridLayout()
        grid.addWidget(btn1, 0, 0)
        grid.addWidget(btn2, 1, 0)
        w1.setLayout(grid)
        self.setCentralWidget(w1)

        btn1.clicked.connect(self.photocall)#connect함수를 통해 연동하기
        btn2.clicked.connect(QCoreApplication.instance().quit)

        self.statusBar()
        self.show()
        self.statusBar().showMessage(self.date.toString(Qt.DefaultLocaleLongDate))  # 상태표시줄에 날짜보여주기

    def buttonClicked(self):
        sender = self.sender()
        self.statusBar().showMessage(sender)


    def photocall(self):
        photo = QCheckBox('사진', self)
        photo.toggle()
        photo.stateChanged.connect(self.changeTitle)

        photomovie = QCheckBox('사진 및 동영상', self)
        photomovie.toggle()
        photomovie.stateChanged.connect(self.changeTitle)


        vbox = QVBoxLayout()
        vbox.addStretch(2)
        vbox.addWidget(photo)
        vbox.addStretch(1)
        vbox.addWidget(photomovie)
        vbox.addStretch(3)


        self.setLayout(vbox)
        self.setWindowTitle('파일 불러오기')
        self.resize(400, 400)
        self.show()


    def changeTitle(self, state):
        if state == Qt.Checked:
            self.setWindowTitle('파일 불러오기')
        else:
            self.setWindowTitle('파일 불러오기')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = picture()
    screen = app.primaryScreen()
    size = screen.size()
    w, h =300, 300
    ex.setGeometry(size.width()/2-w/2, size.height()/2-h/2,w ,h)
    ex.setWindowTitle('picture dimension')
    sys.exit(app.exec_())
