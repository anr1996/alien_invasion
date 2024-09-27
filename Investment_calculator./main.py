# # prompts the user for input.
# # call functions or methods from 'account.py and utils.py.

from account import *
import sys  # Only needed for access to command line arguments

from PyQt6.QtGui import (
    QPixmap
)
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QDateEdit,
    QDateTimeEdit,
    QDial,
    QDoubleSpinBox,
    QFontComboBox,
    QLabel,
    QLCDNumber,
    QLineEdit,
    QMainWindow,
    QProgressBar,
    QPushButton,
    QRadioButton,
    QSlider,
    QSpinBox,
    QTimeEdit,
    QVBoxLayout,
    QWidget,
    QListWidget,
    QVBoxLayout,
    QHBoxLayout,
   )

# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        
        self.setWindowTitle("Investment Calculator")
        
        layout_1 = QVBoxLayout()
        layout_1.setContentsMargins(0,0,0,0)
        layout_1.setSpacing(20)

        intro_widget = QLabel("Welcome to the Investment Calculator. Our tool helps you estimate the costs "  
                        "associated with loans, interest rates, and lines of credit. "
                        "\nEnter your details to explore various financial options and make informed decisions.")


        font = intro_widget.font()
        font.setPointSize(15)
        intro_widget.setFont(font)
       # intro_widget.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)
        
        #widget.setPixmap(QPixmap('AMERICAN-PSYCHO.jpg')) 
        # The image above i will use later,
        # currently too large and covers text so we will need to scale down and move it to another position.
        
        # self.setCentralWidget(intro_widget)
        
        loan_selection = QComboBox()
        loan_selection.addItems([
                                "Annual percentage rate",
                                "Annual percentage yield",
                                "Compound interest rate",
                                "Equity loan",
                                "Heloc line of credit",
                                "Home equity",
                                "Personal loan",
                                "Simple interest rate"
                                ])
                                 
        
        # Sends the current index (position) of the selected item.
        loan_selection.currentIndexChanged.connect(self.index_changed)
        
        loan_selection.setInsertPolicy(QComboBox.InsertPolicy.InsertAlphabetically)
        loan_selection.setFixedSize(200, 30)
        
        layout_1.addWidget(intro_widget)
        layout_1.addWidget(loan_selection)
        #self.setMenuWidget(loan_selection)
        widget = QWidget()
        widget.setLayout(layout_1)
        self.setMenuWidget(widget)
        
     
        
    def index_changed(self, i): # i is an int
        print(i)


app = QApplication(sys.argv)
app.setStyle('Fusion')

window = MainWindow()
window.show() # IMPORTANT!!! Windows are hidden by default.
window.setMinimumSize(400,300)
window.setStyleSheet("""
                     QPushButton:focus { outline: none; }
                     QWidget { background-color: hsl(330, 10%, 20%); }
                     """)

app.exec()

