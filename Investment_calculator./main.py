
# # prompts the user for input.
# # call functions or methods from 'account.py and utils.py.

from account import *
import sys  # Only needed for access to command line arguments

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Investment Calculator")
        
        button = QPushButton("Buy Stocks!")
        
        # Set the central widget of the Window.
        self.setCentralWidget(button)
        
        

app = QApplication(sys.argv)
app.setStyle('Fusion')

window = MainWindow()
window.show() # IMPORTANT!!! Windows are hidden by default.
window.setMinimumSize(400,300)
window.setStyleSheet("""
                     QPushButton:focus { outline: none; }
                     QWidget { background-color: hsl(330, 1%, 30%); }
                     """)

app.exec()

