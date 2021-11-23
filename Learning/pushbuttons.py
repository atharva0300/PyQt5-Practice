from PyQt5.QtWidgets import QApplication, QPushButton, QMainWindow
import sys 
from PyQt5 import QtGui
# importing QRect to set the geometry 
from PyQt5.QtCore import QRect
from PyQt5.QtCore import QSize


# creating class 
class window(QMainWindow): 
    def __init__(self): 
        super().__init__()

        title = 'pyqt5 main window '
        left = 500
        top  =200
        width = 300
        height= 250

        self.setWindowTitle(title)
        self.setWindowIcon(QtGui.QIcon("./icons/file.png"))
        self.setGeometry(left,  top , width , height)

        # Calling the UiComponents function here 
        self.UiComponenets()

        # to show the window 
        self.show()
    
    def UiComponenets(self): 
        button = QPushButton('Click me' , self)
        # name of the button ( tag ) : Click me

        # move the button
        button.move (50,50) 
        # move by x : 50 and y : 50

        # set the geometry of the button
        button.setGeometry(QRect(100 , 100,111 , 50))
        # QRect ( left, top , width , height )
        
        # set the Icon for the push button
        button.setIcon(QtGui.QIcon("./icons/new_file.png"))

        # setting the size of the icon of the push button
        button.setIconSize(QSize(40,40))
        # width  , height

        # Adding a tooltip to the button
        # tooltip : the text that appears, when you hover your cursor over the button
        button.setToolTip('<h2>This is click me button<h2>')
        # here <h2> is the html header 2 tag 


# creating an instance of the class 
if __name__ == "__main__" : 
    App = QApplication(sys.argv)

    # creating window object 
    window = window()

    # exit the application
    sys.exit(App.exec())