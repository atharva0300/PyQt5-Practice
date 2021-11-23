# whats this widget.py 

from PyQt5.QtWidgets import QApplication, QHBoxLayout, QLabel, QMainWindow, QDialog, QPushButton, QVBoxLayout
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

        # show the window 
        self.show()
    
    def initwindow(self): 
        self.setWindowIcon(QtGui.QIcon('./icons/file.png'))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left , self.top , self.width , self.height)


        # creating a hboxlayout 
        hbox = QHBoxLayout()

        label = QLabel('Focus And Press SHIFT + F1')
        hbox.addWidget(label)

        # create a button
        button = QPushButton('Click Me')
        # adding whats this class to the button 
        
        button.setWhatsThis('This is a button that you can click on this')
        hbox.addWidget(button)

        # set the layout to hbox 
        self.setLayout(hbox)

        # show the window 
        self.show()


if __name__ == "__main__": 
    App = QApplication(sys.argv)
    window=  window()
    sys.exit(App.exec())
