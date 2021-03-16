import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget

# Example 1
class Example(QWidget):
    def __init__(self):
        super().__init__()  # super() allow child class to use the method of the parent class.
        self.initUI()

    def initUI(self):
        self.setGeometry(
            300, 300, 300, 220
        )  # (x,y): position on screen, (width, height): window size
        self.setWindowTitle("My window with PyQt5!")
        self.setWindowIcon(QIcon("icons/icon.ico"))
        self.show()


# Modules and functions
def windowFunction():
    window = QtWidgets.QWidget()
    window.setGeometry(200, 200, 500, 300)
    window.setWindowTitle("My 2nd window with PyQt5!")
    window.setWindowIcon(QIcon("icons/icon.ico"))

    # The vidgets
    objectMylabel = QtWidgets.QLabel(window)
    objectMylabel.setText("Python 3")
    objectMylabel.move(200, 20)

    objectMylabel12 = QtWidgets.QLabel(window)
    objectMylabel12.setPixmap(QtGui.QPixmap("icons/potato.ico"))
    objectMylabel12.move(130, 50)

    objectSheep = QtWidgets.QPushButton(window)
    objectSheep.setText("Click me!")
    objectSheep.move(400, 250)
    objectSheep.setGeometry(380, 250, 100, 30)

    # Visualization
    window.show()
    applicationExec = application.exec_()
    sys.exit(applicationExec)


if __name__ == "__main__":

    application = QApplication(sys.argv)

    # # Example 1
    # objectExemple = Example()
    # sys.exit(application.exec_())

    # Example 2
    windowFunction()