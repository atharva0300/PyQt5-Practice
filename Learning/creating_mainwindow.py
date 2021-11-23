from PyQt5.QtWidgets import QMainWindow, QApplication
import sys 
from PyQt5 import QtGui
# importing GUi from PyQt5

# main class 
class window(QMainWindow): 
    # inherting from the MainWindow 
    def __init__(self): 
        super().__init__()

        # givinng title 
        self.title = 'pyqt5 window'

        # giving dimensions to the window 
        self.top = 100
        self.left = 100
        self.width = 400
        self.height = 300

        # calling the window class 
        self.initwindow()

    # creating init window 
    def initwindow(self): 
        # setting icon to the window 
        # importing QtGui for setting the icon
        self.setWindowIcon(QtGui.QIcon("./icons/file.png"))
        self.setWindowTitle(self.title)

        # creating the geometry 
        self.setGeometry(self.left , self.top , self.width, self.height)
        # 4 parameters to the mainwindow geometry height 
        # left , top , width ,height

        # show the window
        # if the self.show() is not mentioned, then the window does not show 
        self.show()
    

# creating object for QApplication
App = QApplication(sys.argv)

window  = window()
# exits the application if there are no errors 
sys.exit(App.exec())

