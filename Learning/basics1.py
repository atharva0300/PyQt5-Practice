import PyQt5.QtWidgets as qtw 
import PyQt5.QtGui as qtg


class MainWindow(qtw.QWidget): 
    def __init__(self ): 
        super().__init__()

        # Add a title
        self.setWindowTitle("Hello World!")

        # Set layout
        self.setLayout(qtw.QVBoxLayout())
        # for the vertical box layout : self.setLayout(qtw.QVBoxLayout())
        # for the horizontal box layout : self.setLayout(qtw.QHBoxLayout())

        # create a label 
        my_label = qtw.QLabel("Atharva here! Good to see you!")
        
        # changing the font size of the label
        my_label.setFont(qtg.QFont('Helvetica' , 18))
        # the font family is : Helvetica 
        # the font size is : 18px 

        my_label2 = qtw.QLabel("Pick a fruit")
        my_label2.setFont(qtg.QFont("Helvetica" , 18))
        # create a Combobox 
        my_combo = qtw.QComboBox(self , editable = True , insertPolicy = qtw.QComboBox.InsertAtTop)
        # making the box editable , editable  = True and insertPolicy = - :: -  , the selected option , gets at the top of the list 
        # insertPolicy = qtw.QComboBox.InsertAtBottom    , inserts the manualy selected , option at the bottom
        # Add items to the combobox 
        my_combo.addItem("Mango" , "something")
        my_combo.addItem("Apple" ,2)
        my_combo.addItem("Grapes" , qtw.QWidget)
        # reference an object to it , here the object is QWidget 
        my_combo.addItem("Guava")
        my_combo.addItems(["One" , "Two" , "Three"])
        # use 'addItem' to add a single value 
        # # use 'addItems' to add a list 
        my_combo.insertItem(2 , "Third thing")
        # insertItem( position , value )   , general syntax 
        # can insert the item in the combo box , at a specifc position
        my_combo.insertItems(3 , ["1" , "2" , "3"])
        # use 'insertItem' to add a single item 
        # use 'insertItems' to add multiple items / container like list
        
        # to put it on the screen, the below code does that
        self.layout().addWidget(my_label)
        self.layout().addWidget(my_label2)
        self.layout().addWidget(my_combo)

        # adding an entry box 
        my_entry  = qtw.QLineEdit()

        # set the name object name of the entry box , to reference it later 
        my_entry.setObjectName("name_field")

        # set the default ( initial ) text in the textbox 
        my_entry.setText("type here")

        # put the entry box on the screen 
        self.layout().addWidget(my_entry)
        # show function() 

        # create a button
        my_button  = qtw.QPushButton("press me!" , clicked = lambda: press_it())
        # set a lambda function , as an action to what will happen, when the button is pressed 

        # put the button on the screen
        self.layout().addWidget(my_button)

        # create aonther button for the combo_box 
        my_button2  = qtw.QPushButton("Confirm fruit!" , clicked = lambda: press_it2())

        # put the button on the screen
        self.layout().addWidget(my_button2)

        # shows the app
        self.show()

        # defining the press_it() function for the entry_box
        def press_it(): 
            # when the button is pressed ,the text form the entry box is taken 
            # and, the label is modified to a new text
            my_label.setText('Hello {0}!' .format(my_entry.text()))

            # clear the entry box 
            my_entry.setText("")
        
        # defining the press_it2) function for the combo box 
        def press_it2(): 
            # when the button is pressed ,the text form the entry box is taken 
            # and, the label is modified to a new text
            my_label2.setText('You picked {0}!' .format(my_combo.currentText()))
            # my_combo.currentText()   : returns the 1st text . Example - ("mango", "something") , this will return only "mango"
            # my_combo.currentData()   : returns the 2nd text. Example - ("mango" , "something")   , this will return only "something"
            # my_combo.currentIndex()  : returns the index of the current item that is selected 

            # clear the entry box 
            my_entry.setText("")



# creating an instance of an app 
app = qtw.QApplication([])
# pass an empty python list , in the aborve , QApplication() fnunction 

# initializing hte main window 
mw= MainWindow()

# Run the App 
app.exec_()