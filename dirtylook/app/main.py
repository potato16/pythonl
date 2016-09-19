import sys
from PyQt5.QtWidgets import (QFrame, QHBoxLayout, QVBoxLayout, 
        QApplication, QWidget)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        #Frame
        leftFrame = QFrame(self)
        leftFrame.setFrameShape(QFrame.StyledPanel)
        midFrame = QFrame(self)
        midFrame.setFrameShape(QFrame.StyledPanel)
        rightFrame = QFrame(self)
        rightFrame.setFrameShape(QFrame.StyledPanel)
        #Layout
        hbox = QHBoxLayout(self)
        hbox.addWidget(leftFrame)
        hbox.addWidget(midFrame)
        hbox.addWidget(rightFrame)
#        hbox = QHBoxLayout(self)
 #       hbox.addWidget(vbox)
        self.setLayout(hbox)
        self.setWindowTitle('Dirty Look')
        self.show()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    sys.exit(app.exec_())



