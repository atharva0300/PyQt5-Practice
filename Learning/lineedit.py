#creating line edit with QLine 
from PyQt5.QtWidgets import QApplication,QLineEdit, QHBoxLayout, QLabel, QMainWindow, QDialog, QVBoxLayout
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

        # setting hbox layout 
        hbox = QHBoxLayout()

        # creating a line edit 
        self.lineedit = QLineEdit(self)
        # adding the line edit to the hbox layout 
        hbox.addWidget(self.lineedit)

        # create a lable 
        self.label = QLabel('Hello')
        
        # set the font of the label 
        self.label.setFont(QtGui.QFont('Sanserif' , 13))

        # add the label to the hbox widget 
        hbox.addWidget(self.label)

        # change the size of the text 
        self.lineedit.setFont(QtGui.QFont('Sanserif' , 13))

        # connect the onPressed function with lineedit 
        self.lineedit.returnPressed.connect(self.OnPresed)

        # set the slef.layout to hbox 
        self.setLayout(hbox)

        # show the window 
        self.show()
    
    def initwindow(self): 
        self.setWindowIcon(QtGui.QIcon('./icons/file.png'))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left , self.top , self.width , self.height)

    def OnPresed(self): 
        # a onpressed function
        self.label.setText(self.lineedit.text())

if __name__ == "__main__": 
    App = QApplication(sys.argv)
    window=  window()
    sys.exit(App.exec())
