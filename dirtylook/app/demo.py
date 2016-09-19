#show image from internet
#show title window with header of wedsite's loaded image

import sys
import urllib.request
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel,
                             QHBoxLayout, QDesktopWidget,
                             QAction, QMainWindow, QScrollArea)
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import Qt
class HatNhan(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        print("Yes")
        pixmap = QPixmap('im.jpg')
        pixmap1= pixmap.scaledToWidth(480)
        #pixmap.loadFromData(data)
        lbl = QLabel(self)
        
        lbl.setPixmap(pixmap1)
        hbox = QHBoxLayout()
        hbox.addWidget(lbl)
       
        self.setLayout(hbox)
        
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        #self.data = data
        self.initUI()
    def initUI(self):
        
        self.statusBar()
        exitAct = QAction(QIcon('exit.png'),'Exit',self)
        exitAct.setShortcut('Ctrl+X')
        exitAct.setStatusTip('Kill me. Ok, go ahead!')
        exitAct.triggered.connect(self.close)
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAct)
        #screen at center
        #fullscreen
        #fullwindow
        #if error when loading image show image holder
        hatnhan = HatNhan()
        #scroll = QScrollArea(hatnhan)
        #scroll.ensureVisible(300, 500, 50, 50)
        #scroll.setWidgetResizable(True)
       # self.center()
        self.setCentralWidget(hatnhan)        
        self.setWindowTitle('Dirty Look')
        self.setGeometry(1,2,3,4)
        self.showMaximized()
        self.center()
        self.show()
        
    def center(self):
            qr = self.frameGeometry()
            cp = QDesktopWidget().availableGeometry().center()
            qr.moveCenter(cp)
            self.move(qr.topLeft())
if __name__=='__main__':
    app = QApplication(sys.argv)
    url = 'https://www.google.com/images/nav_logo242.png'
    #try:
     #   data = urllib.request.urlopen(url).read()
    w = MainWindow()
    #except:
     #   print("Ok great")
    
    
    sys.exit(app.exec_())
    
