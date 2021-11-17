# using the classes , re-creating hte same program of basics2.py here

import sys 
from PyQt5.QtWidgets import QApplication, QGridLayout, QHBoxLayout, QGridLayout ,QMainWindow, QPushButton  , QWidget, QAction
from PyQt5.QtGui import QIcon
from PyQt5.Qt import QLabel , QPushButton , QHBoxLayout , QVBoxLayout
from PyQt5.QtCore import Qt

class GUI(QMainWindow):
    # inherit the QMainWindow 
    def __init__(self): 
        super().__init__()
        # initialize super class , which creates the window 

        self.initUI()
        # refer to window as self

    
    def initUI(self): 

        self.add_menus_and_status()
        # creating a fuction to add menus and status 

        self.setWindowTitle('Window')
        # add widgets and change the properties 

        self.resize(400 ,300)
        # resize hte window(width , height ) 

        self.positional_widget_layout()
        # create a function to give positional widget layout and positioning them
        # using grid 



    def add_menus_and_status(self): 
        self.statusBar().showMessage('Text here, this is a message')
        # displays the message at the status bar ( at the bottom of the window )

        menubar = self.menuBar()
        # create menu bar 

        file_menu = menubar.addMenu('File')
        # adds menu to the menu bar 

        new_icon = QIcon('icons/new_file.png')
        # create icon

        new_action = QAction(new_icon , 'New' , self)
        # create an action and include the icon , action name 
        # NOTE - while practicing the icon dosen't get displayed

        file_menu.addAction(new_action)
        # add the action to the menu 

        new_action.setStatusTip('New File')
        # statusbar updated 

        file_menu.addSeparator()
        # adds a separator line in between the actions 

        exit_icon = QIcon('icons/exit.png')
        exit_action = QAction(exit_icon , 'Exit' , self)
        exit_action.setStatusTip('Exit')

        exit_action.triggered.connect(self.close)
        # close the application when clicked 

        exit_action.setShortcut('Ctrl+Q')
        # sets a shortcut to the keyboard to close the application 
        # and linked it with the action of hte exit_action 


        file_menu.addAction(exit_action)


        edit_menu = menubar.addMenu('Edit')
        # add new menu to the menubar 

        # placing an icon into the menuimport 
        # import the QIcon from PyQt5.QtGui
        # from PyQt5.QtGui import QIcon


        self.resize(400 , 300)
        # resiz the window ( width ,  height)

    def positional_widget_layout(self): 
        label_1 = QLabel('Our first label' ,self)
        # to user QLabel class , import QLabel form PyQt5.Qt
        # from PyQt5.Qt import QLabel
        # label w/out text, window is teh parent

        print(self.menuBar().size())
        # default size : PyQt5.QtCore.QSize(100 , 30)

        mbar_height = self.menuBar().height()
        print(mbar_height)
        label_1.move(10 , mbar_height)
        # align and position below label_l

        label_2 = QLabel('Another Label' , self)
        # create another label

        label_2.move(10 , mbar_height*2 )
        # align and position below label_1

        label_span = QLabel('Label spanning columns span span span span')

        # adding buttons 
        button_1 = QPushButton('click 1' , self)
        button_2 =QPushButton('click 2' , self)

        button_1.move(label_1.width() , label_1.height())
        button_2.move(label_1.width() , label_1.height() * 2)

        grid_layout = QGridLayout()
        # to use QGridLayout , import QGridLayout from PyQt5.QtWidgets
        # from PyQt5.QtWidgets import QGridLayout

        grid_layout.addWidget(label_1 , 0 , 0)
        # row : 0 ,col: 0
        grid_layout.addWidget(button_1 , 0,1)
        # row : 0 ,col: 1
        grid_layout.addWidget(label_2 , 1,0)
        # row : 1 ,col: 0
        grid_layout.addWidget(button_2,1,1)
        # row : 1 ,col: 1

        grid_layout.addWidget(label_span , 2,0,1,3)
        # row  =2 , col = 0 , rowspan = 1 , colspan = 3

        grid_layout.setAlignment(Qt.AlignBottom)
        # aigns the grid at the bottom
        grid_layout.setAlignment(label_1 ,Qt.AlignRight)
        # aligns the label_1 of the grid, to the right 
        grid_layout.setAlignment(label_2,Qt.AlignRight)
        # aligns the labe_2 of the grid to the right 

        # to align the grid at hte top -left position 
        # grid_layout.setAlignment(Qt.AlignTop | Qt.AlignLeft )

        # To use the QtAlign<position>
        # from PyQt5.QtCore import Qt

        # The below code , to set the layout , using horizontal box and vertical box 
        # the above code , to set hte layout , using grid layout 
        '''
        hbox_1 = QHBoxLayout()
        hbox_1.addStretch()
        # pushes /stretches the layout to the right 
        hbox_2 =QHBoxLayout()
        hbox_2.addStretch()
        # pushes /stretches the layout to the right 

        hbox_1.addWidget(label_1)
        hbox_1.addWidget(button_1)

        hbox_2.addWidget(label_2)
        hbox_2.addWidget(button_2)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox_1)
        vbox.addLayout(hbox_2)

        # for push buttons  : import QPushButton
        # for QHBoxLayout  : import QHBoxLayout 
        # for QVBoxLayout : import QVBozLayout 
        # QHBoxLayout : Horizontal Box layout 
        # QVBozLayout : Vertical Box Layout 

        '''


        layout_widget = QWidget() 
        # create QWidget object 

        '''
        layout_widget.setLayout(vbox)
        # for setting vbox layout 
        # set layout 
        '''

        layout_widget.setLayout(grid_layout)
        # for setting grid_layout 

        self.setCentralWidget(layout_widget)
        # make QWidget the central widget 



        label_1.move(10,20)
        # position label below the menubar 
    







if __name__ == '__main__': 
    app =QApplication(sys.argv)
    # create application 

    gui = GUI()
    # create instance class 
    
    gui.show()
    # show the constructor PyQt window 

    sys.exit(app.exec_())
    # execite the application



