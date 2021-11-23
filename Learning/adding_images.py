from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QDialog, QVBoxLayout
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

        # creating vbox 
        vbox = QVBoxLayout()
        labelImage = QLabel(self)

        # creating a pixmap object 
        pixmap = QPixmap('./images/minecraft.jpg')
        labelImage.setPixmap(pixmap)

        # add widget 
        vbox.addWidget(labelImage)

        # set the layout 
        self.setLayout(vbox)



if __name__ == "__main__": 
    App = QApplication(sys.argv)
    window=  window()
    sys.exit(App.exec())
