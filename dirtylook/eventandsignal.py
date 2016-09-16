import sys
from PyQt5.QtCore import Qt, pyqtSignal, QObject
from PyQt5.QtWidgets import (QWidget, QLCDNumber, QSlider,
        QVBoxLayout, QHBoxLayout, QApplication,
        QMainWindow, QPushButton)
class Communicate(QObject):
    closeApp = pyqtSignal()
class EmittingExample(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.c = Communicate()
        self.c.closeApp.connect(self.close)
        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Emit signal')
        self.show()
    def mousePressEvent(self, event):
        self.c.closeApp.emit()
class SenderExample(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        btn1 = QPushButton('Button Ok', self)
        btn1.move(30, 50)
        btn2 = QPushButton('Button 2', self)
        btn2.move(150, 50)
        btn1.clicked.connect(self.buttonClicked)
        btn2.clicked.connect(self.buttonClicked)
        self.statusBar()

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Event handler')
        self.show()
    def buttonClicked(self):
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was pressed')
    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()
class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        lcd = QLCDNumber (self)
        sld = QSlider(Qt.Vertical, self)

        vbox = QHBoxLayout()
        vbox.addWidget(lcd)
        vbox.addWidget(sld)

        self.setLayout(vbox)
        sld.valueChanged.connect(lcd.display)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Signal & slot')
        self.show()
    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = EmittingExample()
    sys.exit(app.exec_())

