#show image from internet
#show title window with header of wedsite's loaded image

import sys
from bs4 import BeautifulSoup
import urllib.request
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel,
                             QHBoxLayout, QDesktopWidget,
                             QAction, QMainWindow, QScrollArea,
                             QMessageBox, QGraphicsScene, QGraphicsView,
                             QGraphicsPixmapItem, QPushButton)
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

        nextImgAct = QAction(QIcon('next.png'),'Next Picture',self)
        nextImgAct.setShortcut('K')
        nextImgAct.setStatusTip('Another one.')
        nextImgAct.triggered.connect(self.timerEvent)
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        toolMenu = menubar.addMenu('&Tool')
        fileMenu.addAction(exitAct)
        toolMenu.addAction(fullscrAct)
        toolMenu.addAction(nextImgAct)
        #screen at center
        #fullscreen
        #fullwindow
        #if error when loading image show image holder
        self.hatnhan = HatNhan()
        self.timer = QBasicTimer()
        self.step =0
        self.delay = 5000
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
    def timerEvent(self, e=None):
        print("start next img")
        self.timer.start(self.delay,self)
        self.tlistlinkindex +=1
        print("reading data")
        data = self.readLinkImage(self.tlistlink[self.tlistlinkindex])
        print("showing data")
        pixmap = QPixmap(data)
        self.hatnhan.setPixmap(pixmap)
        self.timer.stop()
        print("done")
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
class DemoWindow(QWidget):
    def __init__(self,image_files, parent=None):
        QWidget.__init__(self, parent)
        self.tlistlink = []
        self.step =0
        self.image_files = image_files
        s = '<>'*300
        self.label = QLabel(s, self)
        self.label.setGeometry(10, 30, 640, 480)
        self.getData()
        #self.button = QPushButton("start Slide Show", self)
        #self.button.setGeometry(10, 10, 140, 30)
        #self.button.clicked.connect(self.timerEvent)
        #self.timer = QBasicTimer()
        #self.step = 0
        #self.delay= 5000
        #sf = "Slides are shown {} seconds apart"
        #self.setWindowTitle(sf.format(self.delay/1000.0))
    def timerEvent(self, e = None):
        if self.step >= len(self.image_files):
            self.timer.stop()
            self.button.setText('Slide Show Finished')
            return
        self.timer.start(self.delay, self)
        file = self.image_files[self.step]
        image = QPixmap(file)
        self.label.setPixmap(image)
        self.setWindowTitle("{} --> {}".format(str(self.step), file))
        self.step +=1
    def keyPressEvent(self, event):
        key = event.key()
        if key == Qt.Key_Left:
            print("Left")
            self.step -=1
        if key == Qt.Key_Right:
            
            self.step +=1
            print("Right")
        if self.step >=0 and self.step <len(self.tlistlink):
            print("loading")
            file= self.readLinkImage(self.tlistlink[self.step])
            print("loading")
            image = QPixmap()
            image.loadFromData(file)
            print("loading")
            self.label.setPixmap(image)
            

            
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
                result = urllib.request.urlopen(tmp1).read()
                return result
                            
if __name__=='__main__':
    image_files=["a1",'a2','a3','a4','a5','a6','a7','a7','a8','a9']
    app = QApplication([])
   # url = 'https://www.google.com/images/nav_logo242.png'
    #try:
     #   data = urllib.request.urlopen(url).read()
   # w = MainWindow()
    #except:
     #   print("Ok great")
    
    w = DemoWindow(image_files)
    w.setGeometry(100, 100, 700, 500)
    w.show()
    app.exec_()
    #sys.exit(app.exec_())
    
