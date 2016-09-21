import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QDesktopWidget,
                             QHBoxLayout, QMessageBox, QMainWindow, QGraphicsScene,
                             QGraphicsView,QGraphicsPixmapItem)
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import Qt
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
       # self.statusBar()
        pixmap = QPixmap('im.jpg')
        scene = QGraphicsScene()
        view = QGraphicsView(scene)
        item = QGraphicsPixmapItem(pixmap)
        scene.addItem(item)
        view.fitInView(item)
        self.setWindowTitle('OOPs')
        self.setCentralWidget(view)
       
        self.show()
        
if __name__=="__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    sys.exit(app.exec_())

