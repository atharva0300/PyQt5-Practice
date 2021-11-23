from PyQt5.QtWidgets import QApplication, QPushButton, QMainWindow
import sys 
from PyQt5 import QtGui


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

        # calling the funciton to create \a button
        self.createButton()


        # to show the window 
        self.show()

    def createButton(self): 
        # create button here 
        button = QPushButton('Button' , self)

        # move the button 
        button.move(50,50)

        # connecting the pushbutton to the signal
        button.clicked.connect(self.ClickMe)
        # here we are calling the ClickMe function
        # that prints Hello World 


        button2 = QPushButton('Exit' , self)
        button2.move(50,100)

        # connecting the button2 to the signal
        button2.clicked.connect(exit)
        # this exits the application when exit button is pressed 
        # here , exit is an inbuilt function of the PyQt5, so we don't have to attach a self.exit 
        # to it 
        # just exit 
        # only user defined functions are given the self. function 
    
    def ClickMe(self): 
        print("Hello World")

# creating an instance of the class 
if __name__ == "__main__" : 
    App = QApplication(sys.argv)

    # creating window object 
    window = window()

    # exit the application
    sys.exit(App.exec())