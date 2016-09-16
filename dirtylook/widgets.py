import sys
from PyQt5.QtWidgets import (QWidget, QCheckBox, QApplication, 
        QPushButton, QFrame, QSlider, QLabel,
        QGridLayout, QProgressBar,
        QCalendarWidget)
from PyQt5.QtCore import Qt, QBasicTimer, QDate
from PyQt5.QtGui import QColor, QPixmap
class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):

        grid = QGridLayout()
        grid.setSpacing(10)

        sld = QSlider(Qt.Horizontal, self)
        sld.setFocusPolicy(Qt.NoFocus)
        grid.addWidget(sld, 1, 0)
        sld.valueChanged[int].connect(self.changeValue)
        self.label = QLabel(self)
        self.label.setPixmap(QPixmap('mute.png'))
        grid.addWidget(self.label,1,1)

        self.col = QColor(0, 0, 0)
        redb = QPushButton ('Red', self)
        redb.setCheckable(True)
        grid.addWidget(redb,2,0)
        redb.clicked[bool].connect(self.setColor)
        redb = QPushButton('Green', self)
        redb.setCheckable(True)
        grid.addWidget(redb,3,0)
        redb.clicked[bool].connect(self.setColor)

        blueb =QPushButton('Blue', self)
        blueb.setCheckable(True)
        grid.addWidget(blueb,4,0)
        blueb.clicked[bool].connect(self.setColor)

        self.square = QFrame(self)
        grid.addWidget(self.square,2,1,3,1)
        self.square.setStyleSheet("QWidget {background-color: %s }" 
            % self.col.name())
        

        cb = QCheckBox('Show title', self)
        grid.addWidget(cb,5,0)
        cb.toggle()
        cb.stateChanged.connect(self.changeTitle)
        
        #ProgressBar
        self.pbar = QProgressBar(self)
        grid.addWidget(self.pbar,6,0)
        self.btnbar = QPushButton('Start', self)
        grid.addWidget(self.btnbar, 7, 0)
        self.btnbar.clicked.connect(self.doAction)
        self.timer = QBasicTimer()
        self.step = 0
        #Calendar
        cal = QCalendarWidget(self)
        cal.setGridVisible(True)
        grid.addWidget(cal, 8,0)
        cal.clicked[QDate].connect(self.showDate)

        self.lblcal = QLabel(self)
        date = cal.selectedDate()
        self.lblcal.setText(date.toString())
        grid.addWidget(self.lblcal,8,1)
        
        self.setLayout(grid)
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('QCheckBox')
        self.show()
    def showDate(self, date):
        self.lblcal.setText(date.toString())
    def timerEvent(self, e):
        if self.step >= 100:
            self.timer.stop()
            self.btnbar.setText('Fin')
            return
        self.step = self.step +1
        self.pbar.setValue(self.step)
    def doAction(self):
        if self.timer.isActive():
            self.timer.stop()
            self.btnbar.setText('Start')
        else:
            self.timer.start(100, self)
            self.btnbar.setText('Stop')

    def changeValue(self, value):
        if value ==0:
            self.label.setPixmap(QPixmap('mute.png'))
        elif value > 0 and value <= 30:
            self.label.setPixmap(QPixmap('min.png'))
        elif value> 30 and value < 80:
            self.label.setPixmap(QPixmap('med.png'))
        else:
            self.label.setPixmap(QPixmap('max.png'))
    def setColor(self, pressed):
        source = self.sender()
        if pressed:
            val = 255
        else: val =0
        if source.text() == "Red":
            self.col.setRed(val)
        elif source.text() == "Green":
            self.col.setGreen(val)
        else:
            self.col.setBlue(val)
        self.square.setStyleSheet("QFrame { background-color: %s}"
            % self.col.name())
    def changeTitle(self, state):
        if state == Qt.Checked:
            self.setWindowTitle('QCheckBox')
        else:
            self.setWindowTitle('')
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex= Example()
    sys.exit(app.exec_())
