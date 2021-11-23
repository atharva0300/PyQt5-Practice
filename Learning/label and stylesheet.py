from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QDialog, QVBoxLayout
import sys 
from PyQt5 import QtGui
from PyQt5.QtGui import QFont

class window(QDialog): 
    def __init__(self): 
        super().__init__()

        self.title = 'PyQt5 Widow '
        self.left = 500
        self.top = 200
        self.width = 300
        self.height = 250
        self.iconName= './icons/file.png'

        # calling the initwindow function 
        self.initwindow()

    def initwindow(self): 
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left , self.top , self.width , self.height)

        # creating a vbox layout 
        vbox = QVBoxLayout()
        label = QLabel('This is PyQt5 Label') 
        vbox.addWidget(label)

        # adding another lablel 2 
        label2 = QLabel('This is PyQt5 Gui Application Developmet')
        label2.setFont(QFont('Sanserif' , 20))
        # style the label 
        label2.setStyleSheet('color:red')
        
        # adding lablel2 to vbox 
        vbox.addWidget(label2)

        self.setLayout(vbox)

        self.show()



if __name__ == '__main__': 
    App = QApplication(sys.argv)

    window =window()

    sys.exit(App.exec())