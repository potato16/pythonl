import sys 
from PyQt5.QtWidgets import (QApplication, QWidget, QToolTip, QPushButton,
         QMessageBox, QDesktopWidget, QMainWindow,
        qApp, QAction, QTextEdit)
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QCoreApplication #nice try you llt

class WindowWithMain(QMainWindow):
    def __init__ (self):
        super().__init__()
        self.initUI()
    def initUI(self):
        textEdit = QTextEdit()
        self.setCentralWidget(textEdit)
        #exitAction = QAction(QIcon('exit.png'),'&Exit', self)
        #exitAction.setShortcut('Ctrl+Q')
        #exitAction.setStatusTip('Whoops. Exit ')
        #exitAction.triggered.connect(qApp.quit)
        
        exitTool = QAction(QIcon('exit24.png'),'Exit',self)
        exitTool.setShortcut('Ctrl+Q')
        exitTool.setStatusTip('Go to get FreeDom!')
        exitTool.triggered.connect(self.close)
        
        toolbar = self.addToolBar('Exit!')
        toolbar.addAction(exitTool)

        self.statusBar()
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitTool)

        self.setGeometry(300,  300, 250, 150)
        self.setWindowTitle('Idk. Do you!')
        self.show()
class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        QToolTip.setFont(QFont('SansSerif', 30))
        self.setToolTip('This is a <b>QWidget</b> widget')
        btn =  QPushButton('Button', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget! Ahh, so disgusting')
        btn.resize(btn.sizeHint())
        btn.move(50,50)
        ## I Hurt myself today
        btn_e = QPushButton('Want some FreeDom',self)
        btn_e.clicked.connect(QCoreApplication.instance().quit)
        btn_e.setToolTip('AHHH, FREEDOM. THIS IS SPARTA')
        btn_e.resize(btn_e.sizeHint())
        btn_e.move(123,123)

        self.resize(250, 150)
        self.center()
        self.setWindowTitle('I not your fucking puppet')
        self.setWindowIcon(QIcon('web.png'))
        self.show()
    def closeEvent(self, event): # You put this like to my face withou
        #any description. Really 
        print('oh, ok. im out')
        reply = QMessageBox.question(self,'Tin Nhan',
                "%EMYEU% than men. Love you!", QMessageBox.Yes | 
                QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

if __name__=='__main__':
    app = QApplication(sys.argv)

    w= WindowWithMain()

    sys.exit(app.exec_())
