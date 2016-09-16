import sys
from PyQt5.QtWidgets import (QWidget, QCheckBox, QApplication, 
        QPushButton, QFrame )
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.col = QColor(0, 0, 0)
        redb = QPushButton ('Red', self)
        redb.setCheckable(True)
        redb.move(10, 10)
        redb.clicked[bool].connect(self.setColor)
        redb = QPushButton('Green', self)
        redb.setCheckable(True)
        redb.move(10, 60)
        redb.clicked[bool].connect(self.setColor)

        blueb =QPushButton('Blue', self)
        blueb.setCheckable(True)
        blueb.move(10, 110)
        blueb.clicked[bool].connect(self.setColor)

        self.square = QFrame(self)
        self.square.setGeometry(150, 20, 100, 100)
        self.square.setStyleSheet("QWidget {background-color: %s }" 
            % self.col.name())
        

        cb = QCheckBox('Show title', self)
        cb.move(20, 20)
        cb.toggle()
        cb.stateChanged.connect(self.changeTitle)
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('QCheckBox')
        self.show()
    def setColor(self, pressed):
        source = self.sender()
        if pressed:
            val = 255
        else: val =0
        if source.text() == "Red":
            self.col.setRed(val)
        elif source.text() == "Green":
            self.col.setGreen(val)
        else:
            self.col.setBlue(val)
        self.square.setStyleSheet("QFrame { background-color: %s}"
            % self.col.name())
    def changeTitle(self, state):
        if state == Qt.Checked:
            self.setWindowTitle('QCheckBox')
        else:
            self.setWindowTitle('')
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex= Example()
    sys.exit(app.exec_())
