from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QHBoxLayout, QMainWindow, QGroupBox, QDialog, QRadioButton, QVBoxLayout
import sys 
from PyQt5 import QtGui
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtCore import QSize


class window(QDialog): 
    def __init__(self): 
        super().__init__()

        self.title = 'PyQt5 Widow '
        self.left = 500
        self.top = 400
        self.width = 400
        self.height =400
        self.iconName= './icons/file.png'

        # calling the initwindow function 
        self.initWindow()

        
        
    
    def initWindow(self): 
        self.setWindowIcon(QtGui.QIcon('./icons/file.png'))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left , self.top , self.width , self.height)

        self.radioButton()

        #creating a vbox layout 
        vbox = QVBoxLayout()
        # add radiobuttonn to the vbox 
        vbox.addWidget(self.groupBox)

        # creating a label 
        self.label = QLabel('Hello')

        # Setting the font to the label 
        self.label.setFont(QtGui.QFont('Sanserif' , 13))

        # adding the label to the widget 
        vbox.addWidget(self.label)

        # set the layout to vbox 
        self.setLayout(vbox)

        # show the window 
        self.show()


    def radioButton(self): 
        self.groupBox = QGroupBox('What is your favourite programming language ? ')
        self.groupBox.setFont(QtGui.QFont('Sanserif' ,13))

        # creating a hboxlayout 
        hboxLayout = QHBoxLayout()

        self.radiobtnl = QRadioButton('Football')
        # set the radio utton ot checked by default 

        self.radiobtnl.setChecked(True)

        # set the icon for the radio button
        self.radiobtnl.setIcon(QtGui.QIcon('./icons/exit.png'))

        # set the icon size 
        self.radiobtnl.setIconSize(QSize(40,40))

        # set the font size of the label 
        self.radiobtnl.setFont(QtGui.QFont('Sanserif', 13))

        # creating toggle signal 
        self.radiobtnl.toggled.connect(self.OnRadioBtn)
        # When the radiobutto1 is clicked ,then 
        # calls the OnRadioBtn function 


        # add radiobutton to the hboxlayout 
        hboxLayout.addWidget(self.radiobtnl)

        # ADDING RADIOBUTTON 2 -------------

        self.radiobtn2 = QRadioButton('Cricket')
        # set the radio utton ot checked by default 

        self.radiobtn2.setChecked(False)
        # unckecked by default 

        # set the icon for the radio button
        self.radiobtn2.setIcon(QtGui.QIcon('./icons/exit.png'))

        # set the icon size 
        self.radiobtn2.setIconSize(QSize(40,40))

        # set the font size of the label 
        self.radiobtn2.setFont(QtGui.QFont('Sanserif', 13))

        self.radiobtn2.toggled.connect(self.OnRadioBtn)
        # When the radiobutto1 is clicked ,then 
        # calls the OnRadioBtn function 

        # add radiobutton to the hboxlayout 
        hboxLayout.addWidget(self.radiobtn2)

        # ADDING RADIOBUTTON 3-----------

        self.radiobtn3 = QRadioButton('Table Tennis')
        # set the radio utton ot checked by default 

        self.radiobtn3.setChecked(False)
        # unckecked by default 

        # set the icon for the radio button
        self.radiobtn3.setIcon(QtGui.QIcon('./icons/exit.png'))

        # set the icon size 
        self.radiobtn3.setIconSize(QSize(40,40))

        # set the font size of the label 
        self.radiobtn3.setFont(QtGui.QFont('Sanserif', 13))

        self.radiobtn3.toggled.connect(self.OnRadioBtn)
        # When the radiobutto1 is clicked ,then 
        # calls the OnRadioBtn function 

        # add radiobutton to the hboxlayout 
        hboxLayout.addWidget(self.radiobtn3)

        # ------------------- # 

        # set layout to the groupBox 
        self.groupBox.setLayout(hboxLayout)

    
    # create a new button for toggling 
    def OnRadioBtn(self): 
        radioBtn =self.sender()

        if radioBtn.isChecked(): 
            # if the radio button is checked 
            # then the label text will change 
            self.label.setText("You have selected " + radioBtn.text())


if __name__ == "__main__": 
    App = QApplication(sys.argv)
    window=  window()
    sys.exit(App.exec())
