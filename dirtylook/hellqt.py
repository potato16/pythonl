import sys 
from PyQt5.QtWidgets import (QApplication, QWidget, QToolTip, QPushButton,
         QMessageBox, QDesktopWidget, QMainWindow,
        qApp, QAction, QTextEdit,
        QLabel, QHBoxLayout, QVBoxLayout, QGridLayout,
        QLineEdit)
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QCoreApplication #nice try you llt

class ReviewLayoutWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        title = QLabel('Title')
        author= QLabel('Author')
        review = QLabel('Review')

        titleEdit = QLineEdit()
        authorEdit = QLineEdit()
        reviewEdit = QTextEdit()

        grid =QGridLayout()
        grid.setSpacing(10)
        grid.addWidget(title,1,0)
        grid.addWidget(titleEdit, 1, 1)

        grid.addWidget(author, 2, 0)
        grid.addWidget(authorEdit, 2, 1)
        grid.addWidget(review, 3, 0)
        grid.addWidget(reviewEdit, 3, 1, 5, 1)
        self.setLayout(grid)
        self.setGeometry(300, 300, 250, 300)
        self.setWindowTitle('Review')
        self.show()
class GridLayoutWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        grid =QGridLayout()
        self.setLayout(grid)

        names= ['Cls', 'Bck','', 'Close',
                '7', '8', '9', '/',
                '4', '5', '6', '*',
                '1', '2', '3', '-',
                '0', '.', '=', '+']
        positions = [(i,j) for i in range (5) for j in range(4)]
        for position, name in zip(positions, names):
            if name =='':
                continue
            button = QPushButton(name)
            grid.addWidget(button, *position)
        self.move(300, 150)
        self.setWindowTitle('Calculator')
        self.show()

class BoxLayoutWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        okButton = QPushButton("OK")
        cancelButton = QPushButton('Cancel')

        hbox =QHBoxLayout()
        hbox.addStretch(1)#What the fuck is this shit?
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)

        vbox = QVBoxLayout()
        vbox.addStretch(1)##??
        vbox.addLayout(hbox)

        self.setLayout(vbox)

        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Buttons')
        self.show()

class LayoutWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        lbl1 = QLabel('ChocLat',self)
        lbl1.move(15, 10)

        lbl2 = QLabel('tutorials', self)
        lbl2.move(35, 40)

        lbl3 = QLabel('for programmers', self)
        lbl3.move(55, 70)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Absolute')
        self.show()

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

    w= ReviewLayoutWindow()

    sys.exit(app.exec_())
