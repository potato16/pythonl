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
class DemoWindow(QWidget):
    def __init__(self,image_files, parent=None):
        QWidget.__init__(self, parent)
        self.tlistlink = []
        self.step =0
        self.image_files = image_files
        s = '<>'*300
        self.label = QLabel(s, self)
        self.label.setGeometry(10, 30, 640, 480)
        scroll = QScrollArea(self)
        hbox = QHBoxLayout(self)
        self.setLayout(hbox)
        hbox.addWidget(scroll)
        scroll.setWidgetResizable(True)
        scrollContent = QWidget(scroll)
        scrollLayout = QHBoxLayout(scrollContent)
        scrollContent.setLayout(scrollLayout)
        scrollLayout.addWidget(self.label)
        scroll.setWidget(scrollContent)
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
  
        if key == Qt.Key_Left and self.step>0:
            print("Left")
            self.step -=1
            self.loadImgToLabel()
        if key == Qt.Key_Right and self.step<len(self.tlistlink):
            self.step +=1
            print("Right")
            self.loadImgToLabel()
        if key == Qt.Key_F11:            
            self.showFullScreen()
        if key == Qt.Key_F10:
            self.showNormal()
    def loadImgToLabel(self):
        print("loading")       
        try:
            file= self.readLinkImage(self.tlistlink[self.step])
            image = QPixmap()
            image.loadFromData(file)
            self.label.setPixmap(image)
            self.label.setFixedSize(image.size())
        except:
            print("Cant load")
        print("done")        
           
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
    
    scroll = QScrollArea()
    w = DemoWindow(image_files)
    scroll.setWidget(w)
    w.setGeometry(100, 100, 700, 500)
    w.show()
    app.exec_()
    #sys.exit(app.exec_())
