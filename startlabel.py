import sys
from PyQt5.QtWidgets import QApplication, QPushButton, QWidget, QCheckBox, QHBoxLayout, QVBoxLayout, QGridLayout
from PyQt5.QtCore import Qt, QCoreApplication
from tkinter import *

class nextcall(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        photo = QCheckBox('사진', self)
        photo.toggle()
        photo.stateChanged.connect(self.changeTitle)

        photomovie = QCheckBox('사진 및 동영상', self)
        photomovie.toggle()
        photomovie.stateChanged.connect(self.changeTitle)

        nextButton = QPushButton('다음', self)
        cancelButton = QPushButton('취소', self)
        nextButton.resize(nextButton.sizeHint())
        cancelButton.clicked.connect(QCoreApplication.instance().quit)


        vbox = QVBoxLayout()
        vbox.addStretch(2)
        vbox.addWidget(photo)
        vbox.addStretch(1)
        vbox.addWidget(photomovie)
        vbox.addStretch(3)
        vbox.addWidget(nextButton)
        vbox.addWidget(cancelButton)

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
    ex = nextcall()
    sys.exit(app.exec_())