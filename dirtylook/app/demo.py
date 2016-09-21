#show image from internet
#show title window with header of wedsite's loaded image

import sys
from bs4 import BeautifulSoup
import urllib.request
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel,
                             QHBoxLayout, QDesktopWidget,
                             QAction, QMainWindow, QScrollArea,
                             QMessageBox, QGraphicsScene, QGraphicsView,
                             QGraphicsPixmapItem)
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import Qt, QBasicTimer

class LabelImg(QLabel):
    def mouseReleaseEvent(self, event):
        #something you want to do here
        None
    
class HatNhan(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        
        self.pixmap = QPixmap('im.jpg')
        #pixmap1= pixmap.scaledToWidth(480)
        #pixmap.loadFromData(data)
        self.lbl = LabelImg(self)
        
        self.lbl.setPixmap(self.pixmap)
        hbox = QHBoxLayout()
        hbox.addWidget(self.lbl)
        
        
        self.setLayout(hbox)
    def lblClicked(self):
        print("Lbl clicked!")
    def loadImage(self, data):
        self.pixmap.loadFromData(data)
        self.lbl.setPixmap(self.pixmap)
        #self.show()
       
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.tlistlink=[]
        self.tlistlinkindex = 0
        #self.data = data
        self.initUI()
    def initUI(self):
        
        self.statusBar()
        #action and shortcut
        exitAct = QAction(QIcon('exit.png'),'Exit',self)
        exitAct.setShortcut('Ctrl+X')
        exitAct.setStatusTip('Kill me. Ok, go ahead!')
        exitAct.triggered.connect(self.close)

        fullscrAct = QAction(QIcon('fullscreen.png'),'Full Screen',self)
        fullscrAct.setShortcut('Ctrl+F')
        fullscrAct.setStatusTip('Show Time!')
        fullscrAct.triggered.connect(self.fullScreenOrNot)
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        toolMenu = menubar.addMenu('&Tool')
        fileMenu.addAction(exitAct)
        toolMenu.addAction(fullscrAct)
        #screen at center
        #fullscreen
        #fullwindow
        #if error when loading image show image holder
        self.hatnhan = HatNhan()
        #scroll = QScrollArea(hatnhan)
        #scroll.ensureVisible(300, 500, 50, 50)
        #scroll.setWidgetResizable(True)
        self.center()
        #self.pixmap = QPixmap('im.jpg')
        #scene = QGraphicsScene()
        #view = QGraphicsView(scene)
        #self.item = QGraphicsPixmapItem(self.pixmap)
        #scene.addItem(self.item)
        #view.fitInView(self.item)
        self.setCentralWidget(self.hatnhan)        
        self.setWindowTitle('Dirty Look')
        self.setGeometry(1,2,3,4)
        
        
        #self.hatnhan.showFullScreen()

        ######################################
        
        self.getData()
        #print(self.tlistlink[self.tlistlinkindex])
        self.hatnhan.loadImage(self.readLinkImage(self.tlistlink[self.tlistlinkindex]))
        #self.item.setPixmap(self.pixmap)
        #scene.addItem(QGraphicsPixmapItem(pixmap))
        ######################################
        self.center()
        self.show()
        
    def center(self):
            qr = self.frameGeometry()
            cp = QDesktopWidget().availableGeometry().center()
            qr.moveCenter(cp)
            self.move(qr.topLeft())
    def fullScreenOrNot(self):
      #  if self.isFullScreen():
     #       self.showNormal()
    #        self.center()
   #     else:
  #          self.showFullScreen()
        print('loading')
        
        self.tlistlinkindex +=1
        pixmap = QPixmap()
        pixmap.loadFromData(self.readLinkImage(self.tlistlink[self.tlistlinkindex]))
        
       
        print("loaded, showing")
       
        self.hatnhan.setPixmap(pixmap)
        
        #print("loaded, showing")
        #self.item.setPixmap(pixmap)
        print('done')
    def keyPressEvent(self, event):
        key = event.key()
        if key == Qt.Key_Left:
            print("Left")
        if key == Qt.Key_Right:
            print('loading')
            self.tlistlinkindex +=1
            self.pixmap.loadFromData(self.readLinkImage(self.tlistlink[self.tlistlinkindex]))
            self.item.setPixmap(pixmap)
            print('dont')
#real shit is here
            
    def getData(self):
        url = 'http://www.nyaa.se/?cats=4_0'
        data = urllib.request.urlopen(url).read()
        soup = BeautifulSoup(str(data),'html.parser')
        for link in soup.find_all('a'):
            tmp = link.get('href')
            if "view&tid" in tmp:
                self.tlistlink.append('http:'+tmp)
        #print(self.tlistlink)
    def readLinkImage(self, url):
        data = urllib.request.urlopen(url).read()
        soup = BeautifulSoup(str(data),'html.parser')
        for link in soup.find_all('img'):
            tmp = link.get('alt')
            tmp1 = link.get('src')
            if 'Image' in tmp:
                print(tmp1)
                return urllib.request.urlopen(tmp1).read()
if __name__=='__main__':
    app = QApplication(sys.argv)
    url = 'https://www.google.com/images/nav_logo242.png'
    #try:
     #   data = urllib.request.urlopen(url).read()
    w = MainWindow()
    #except:
     #   print("Ok great")
    
    
    sys.exit(app.exec_())
    
