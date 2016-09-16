import sys
from PyQt5.QtWidgets import (QWidget, QHBoxLayout,
        QLabel, QApplication, QLineEdit,
        QFrame, QSplitter, QStyleFactory,
        QComboBox)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        topleft = QFrame(self)
        topleft.setFrameShape(QFrame.StyledPanel)
        topright = QFrame(self)
        topright.setFrameShape(QFrame.StyledPanel)
        bottom = QFrame(self)
        bottom.setFrameShape(QFrame.StyledPanel)
        splitter1 = QSplitter(Qt.Horizontal)
        splitter1.addWidget(topleft)
        splitter1.addWidget(topright)
        splitter2 = QSplitter(Qt.Vertical)
        splitter2.addWidget(splitter1)
        splitter2.addWidget(bottom)
        self.lbl1 = QLabel(self)
        qle = QLineEdit(self)
        qle.move(60, 100)
        self.lbl1.move(60,40)
        qle.textChanged[str].connect(self.onChanged)
        hbox = QHBoxLayout(self)
        hbox.addWidget(splitter2)
        #combobox
        self.lblc = QLabel('Ubuntu', self)
        combo = QComboBox(self)
        combo.addItem("Ubuntu")
        combo.addItem("Mandriva")
        combo.addItem("Fedora")
        combo.addItem("Arch")
        combo.addItem("Gentoo")
        combo.move (50, 50)
        self.lblc.move(50,150)
        combo.activated[str].connect(self.onActivated)
        tmphbox = QHBoxLayout()
        tmphbox.addWidget(combo)
        tmphbox.addWidget(self.lblc)
        topleft.setLayout(tmphbox)
        #hbox.addWidget(self.lbl1)
        #hbox.addWidget(qle)
        pixmap = QPixmap('img1.jpg')
        lbl = QLabel(self)
        
        lbl.setPixmap(pixmap)
        #hbox.addWidget(lbl)
        self.setLayout(hbox)
       # self.move(300, 200)
        tmphbox = QHBoxLayout()
        tmphbox.addWidget(self.lbl1)
        tmphbox.addWidget(qle)
        topright.setLayout(tmphbox)
        tmphbox = QHBoxLayout()
        tmphbox.addWidget(lbl)
        bottom.setLayout(tmphbox) 
        self.setWindowTitle('Red Rock')
        
        self.show()
    def onActivated(self, text):
        self.lblc.setText(text)
        self.lblc.adjustSize()
    def onChanged(self, text):
        self.lbl1.setText(text)
        self.lbl1.adjustSize()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
