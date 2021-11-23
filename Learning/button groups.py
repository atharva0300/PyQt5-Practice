# Button Groups in Python
import PyQt5
from PyQt5.QtWidgets import QApplication, QHBoxLayout, QLabel, QButtonGroup, QMainWindow, QDialog, QPushButton, QVBoxLayout
import sys 
from PyQt5 import QtGui
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtCore import QSize

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

        # creata a label
        self.label = QLabel('Hello')
        self.label.setFont(QtGui.QFont('Sanserif' , 13))
        self.hbox.addWidget(self.label)

        # set the self.layout to hbox 
        self.setLayout(self.hbox)

        # calling the onPresed function
        self.on_Pressed()

        # show the window 
        self.show()
    
    def initwindow(self): 
        self.setWindowIcon(QtGui.QIcon('./icons/file.png'))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left , self.top , self.width , self.height)


        # create a Hbox layout 
        self.hbox = QHBoxLayout()

        # create a button group
        self.buttongroup = QButtonGroup()

        # connecting the button group with signal 
        self.buttongroup.buttonClicked[int].connect(self.on_Pressed)

        # create 3 buttons 
        self.button1 = QPushButton('Python')

        # add button1 to the Button Group
        self.buttongroup.addButton(self.button1 , 1)

        self.button1.setIcon(QtGui.QIcon('./icons/python.png'))
        self.button1.setIconSize(QSize(40,40))

        # ---------- # 
        # add the button group to hbox layout 
        self.hbox.addWidget(self.button1)


        # Button 2 ----

        self.button2 = QPushButton('C++')

        # add button1 to the Button Group
        self.buttongroup.addButton(self.button2 , 2)

        self.button2.setIcon(QtGui.QIcon('./icons/cpp.png'))
        self.button2.setIconSize(QSize(40,40))

        # ---------- # 
        # add the button group to hbox layout 
        self.hbox.addWidget(self.button2)

        # Button 3 ---

        self.button3 = QPushButton('Java')

        # add button1 to the Button Group
        self.buttongroup.addButton(self.button3 , 3)

        self.button3.setIcon(QtGui.QIcon('./icons/java.png'))
        self.button3.setIconSize(QSize(40,40))

        # ---------- # 
        # add the button group to hbox layout 
        self.hbox.addWidget(self.button3)
    
    def on_Pressed(self):
        
        for button in self.buttongroup.buttons(): 
            if button is self.buttongroup.button(id) : 
                # give the text an id in the above line
                self.label.setText(button.text() + ' Was clicked')



if __name__ == "__main__": 
    App = QApplication(sys.argv)
    window=  window()
    sys.exit(App.exec())
