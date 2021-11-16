from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import uic
import sys


class AppDemo(QWidget): 
    def __init__(self): 
        super().__init__()
        uic.loadUi('test1.ui' , self)

        self.button.clicked.connect(self.printValue)
    
    def printValue(self): 
        print(self.entry1.text())


if __name__ == '__main__': 
    app = QApplication(sys.argv)
    demo = AppDemo()
    demo.show()

    try : 
        sys.exit(app.exec_())
    except SystemExit : 
        print("Closing Window...")
    