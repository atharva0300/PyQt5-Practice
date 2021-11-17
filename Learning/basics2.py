import sys 
from PyQt5.QtWidgets import *

app  = QApplication(sys.argv)
# creating the instance of the QApplication class 
# and initializing to a variable named 'app'

# creating the instance of the QWidgets classs to a variable named 'win'
win = QWidget()
# this creates the top level window 

# adding title to the window 
win.setWindowTitle('Window')

# added the dimensions to the window 
win.resize(400 , 300)
# width x length 


win.show()
# shows the application


sys.exit(app.exec_())
# ensures that any error , that occurs gets handled 

# Qt exec_ ends with an underscore 
app.exec_()


app.exec()
# executes the application ( exec is a keyword )




