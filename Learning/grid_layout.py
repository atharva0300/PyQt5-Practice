from PyQt5.QtWidgets import QApplication, QDialog, QGridLayout, QPushButton, QMainWindow, QVBoxLayout
import sys 
from PyQt5 import QtGui 
from PyQt5.QtWidgets import QGroupBox
from PyQt5.QtWidgets import QDialog
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout



# creating class 
class window(QDialog): 
    def __init__(self): 
        super().__init__()

        # givinng title 
        self.title = 'pyqt5 window'

        # giving dimensions to the window 
        self.top = 100
        self.left = 100
        self.width = 400
        self.height = 300

        # calling the initwindow 
        self.initwindow()

    def initwindow(self): 
        # setting icon to the window 
        # importing QtGui for setting the icon
        self.setWindowIcon(QtGui.QIcon("./icons/file.png"))
        self.setWindowTitle(self.title)

        # creating the geometry 
        self.setGeometry(self.left , self.top , self.width, self.height)
        # 4 parameters to the mainwindow geometry height 
        # left , top , width ,height


        # Calling the gridLayout 
        self.Createlayout()
        vbox = QVBoxLayout()
        vbox.addWidget(self.groupBox)

        # set layout of the window to our vbox 
        self.setLayout(vbox)
        # show the window
        # if the self.show() is not mentioned, then the window does not show 
        self.show()
    
    # creating a function for layout 
    def Createlayout(self): 
        self.groupBox = QGroupBox('What is your favourite programming language ? ')
        gridLayout = QGridLayout()

        button1 = QPushButton('Python' , self)
        button1.setIcon(QIcon('./icons/python.png'))
        button1.setIconSize(QSize(40,40))
        button1.setMinimumHeight(40)
        gridLayout.addWidget(button1 , 0,0)

        button2 = QPushButton('C++' , self)
        button2.setIcon(QIcon('./icons/cpp.png'))
        button2.setIconSize(QSize(40,40))
        button2.setMinimumHeight(40)
        gridLayout.addWidget(button2 , 0,1)

        button3 = QPushButton('Java' , self)
        button3.setIcon(QIcon('./icons/java.png'))
        button3.setIconSize(QSize(40,40))
        button3.setMinimumHeight(40)
        gridLayout.addWidget(button3 , 1,0)

        button4 = QPushButton('C#' , self)
        button4.setIcon(QIcon('./icons/c#.png'))
        button4.setIconSize(QSize(40,40))
        button4.setMinimumHeight(40)
        gridLayout.addWidget(button4 , 1,1)

        self.groupBox.setLayout(gridLayout)





# creating an instance of the class 
if __name__ == "__main__" : 
    App = QApplication(sys.argv)

    # creating window object 
    window = window()

    # exit the application
    sys.exit(App.exec())