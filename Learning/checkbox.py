from PyQt5.QtWidgets import QApplication, QCheckBox, QGroupBox, QHBoxLayout, QLabel, QMainWindow, QDialog, QVBoxLayout
import sys 
from PyQt5 import QtGui
from PyQt5.QtGui import QFont
from PyQt5 import QtCore

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

        # calling checkBox function 
        self.checkBox()

        # creating a vbox layout 
        vbox = QVBoxLayout()

        # add group box to vbox 
        vbox.addWidget(self.groupbox)

        # create label 
        self.label = QLabel('Hello')

        # set the font of the label 
        self.label.setFont(QtGui.QFont('Sanserif' , 13))

        # add the label to the vbox 
        vbox.addWidget(self.label)

        # calling the OnChecked_Toggle function 
        self.OnChecked_Toggled()

        # set the layout to vbox 
        self.setLayout(vbox)

        # showing the window 
        self.show()
    

    def checkBox(self): 

        # creating a group box 
        self.groupbox= QGroupBox("What is your Favourite Programming Language ? ")

        # set the font for the group box 
        self.groupbox.setFont(QtGui.QFont('Sanserif' , 13))

        # create hbox layout 
        hboxlayout = QHBoxLayout()

        # CHECKBOX 1 --------------

        # creating checkBox 
        self.checkbox1 = QCheckBox('Python')

        # set the icon for checkbox
        self.checkbox1.setIcon(QtGui.QIcon('./icons/python.png'))

        # setting the icon size 
        self.checkbox1.setIconSize(QtCore.QSize(40,40))

        # set the font of the checkbox text 
        self.checkbox1.setFont(QtGui.QFont('Sanserif' , 13))

        # when the checkbox1 is toggled, then execute the OnChecked_Toggled function
        self.checkbox1.toggled.connect(self.OnChecked_Toggled)

        # adding the checkbox1 to the hboxlayout 
        hboxlayout.addWidget(self.checkbox1)

        # CHECKBOX 2 --------------

        # creating checkBox 
        self.checkbox2 = QCheckBox('C++')

        # set the icon for checkbox
        self.checkbox2.setIcon(QtGui.QIcon('./icons/cpp.png'))

        # setting the icon size 
        self.checkbox2.setIconSize(QtCore.QSize(40,40))

        # set the font of the checkbox text 
        self.checkbox2.setFont(QtGui.QFont('Sanserif' , 13))

        # when the checkbox2 is toggled, then execute the OnChecked_Toggled function
        self.checkbox2.toggled.connect(self.OnChecked_Toggled)

        # adding the checkbox1 to the hboxlayout 
        hboxlayout.addWidget(self.checkbox2)

        # CHECKBOX 3 --------------

        # creating checkBox 
        self.checkbox3 = QCheckBox('Java')

        # set the icon for checkbox
        self.checkbox3.setIcon(QtGui.QIcon('./icons/java.png'))

        # setting the icon size 
        self.checkbox3.setIconSize(QtCore.QSize(40,40))

        # set the font of the checkbox text 
        self.checkbox3.setFont(QtGui.QFont('Sanserif' , 13))

        # when the checkbox3 is toggled, then execute the OnChecked_Toggled function
        self.checkbox3.toggled.connect(self.OnChecked_Toggled)

        # adding the checkbox1 to the hboxlayout 
        hboxlayout.addWidget(self.checkbox3)

        # CHECKBOX 4 --------------

        # creating checkBox 
        self.checkbox4 = QCheckBox('C#')

        # set the icon for checkbox
        self.checkbox4.setIcon(QtGui.QIcon('./icons/c#.png'))

        # setting the icon size 
        self.checkbox4.setIconSize(QtCore.QSize(40,40))

        # set the font of the checkbox text 
        self.checkbox4.setFont(QtGui.QFont('Sanserif' , 13))

        # when the checkbox4 is toggled, then execute the OnChecked_Toggled function
        self.checkbox4.toggled.connect(self.OnChecked_Toggled)

        # adding the checkbox1 to the hboxlayout 
        hboxlayout.addWidget(self.checkbox4)

        # --------------------- # 

        # set groupbox layout 
        self.groupbox.setLayout(hboxlayout)
    
    def OnChecked_Toggled(self): 
        # a function, to execute, when the checkbox is toggled 
        if self.checkbox1.isChecked(): 
            self.label.setText('You have selected : ' + self.checkbox1.text())
        
        if self.checkbox2.isChecked(): 
            self.label.setText('You have selected : ' + self.checkbox2.text())
        
        if self.checkbox3.isChecked(): 
            self.label.setText('You have selected : ' + self.checkbox3.text())
        
        if self.checkbox4.isChecked(): 
            self.label.setText('You have selected : ' + self.checkbox4.text())
        

        

if __name__ == '__main__': 
    App = QApplication(sys.argv)

    window =window()

    sys.exit(App.exec())