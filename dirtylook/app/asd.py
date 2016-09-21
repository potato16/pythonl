import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QDesktopWidget,
                             QHBoxLayout, QMessageBox, QMainWindow, QGraphicsScene,
                             QGraphicsView,QGraphicsPixmapItem)
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import Qt

app = QApplication(sys.argv)
scn = QGraphicsScene()
view = QGraphicsView(scn)

pixmap = QPixmap("im.jpg")
pixItem = QGraphicsPixmapItem(pixmap)

scn.addItem(pixItem)
view.fitInView(pixItem)
#view.fitInView(gfxPixItem) # Crashes, see below for call stack in OSX
view.show()

sys.exit(app.exec_())
