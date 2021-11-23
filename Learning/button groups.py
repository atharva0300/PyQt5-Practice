# Button Groups in Python
from PyQt5.QtWidgets import QApplication, QHBoxLayout, QLabel, QButtonGroup, QMainWindow, QDialog, QPushButton, QVBoxLayout
import sys 
from PyQt5 import QtGui
from PyQt5.QtGui import QFont, QPixmap

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

        # set the self.layout to hbox 

        # create a vbox 
        vbox = QVBoxLayout()
        self.setLayout(vbox)

        # show the window 
        self.show()
    
    def initwindow(self): 
        self.setWindowIcon(QtGui.QIcon('./icons/file.png'))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left , self.top , self.width , self.height)


        # create a Hbox layout 
        hbox = QHBoxLayout()

        # create a button group

        self.buttongroup = QButtonGroup()

        # create 3 buttons 
        self.button1 = QPushButton('Python')

        # add button1 to the Button Group
        self.buttongroup.addButton(self.button1 , 1)

        # add the button group to hbox layout 
        hbox.addWidget(self.buttongroup)



if __name__ == "__main__": 
    App = QApplication(sys.argv)
    window=  window()
    sys.exit(App.exec())
