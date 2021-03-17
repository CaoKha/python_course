from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMessageBox


class windowMain(QtWidgets.QWidget):
    def __init__(self):
        super(windowMain, self).__init__()
        self.initialisationInterface()

    def initialisationInterface(self):
        self.setGeometry(200, 200, 400, 100)
        self.setWindowTitle("My 2nd window in PyQt5!")
        self.setWindowIcon(QIcon("icons/potato.ico"))

        # The vidgets
        self.objectMyLabel = QtWidgets.QLabel("Python 3: Utilization of MessageBox")
        self.objectMyEraseButton = QtWidgets.QPushButton("Erase")
        self.objectMyCopyButton = QtWidgets.QPushButton("Copy")
        self.objectMyLineEdit = QtWidgets.QLineEdit(
            "Type the message you want copying!"
        )

        # The placement of vidgets
        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.objectMyLabel)
        v_box.addWidget(self.objectMyLineEdit)
        v_box.addWidget(self.objectMyEraseButton)
        v_box.addWidget(self.objectMyCopyButton)

        # Mail application
        self.setLayout(v_box)

        # Connect events to buttons handlers
        self.objectMyCopyButton.clicked.connect(self.CopyClickedHandler)
        self.objectMyEraseButton.clicked.connect(self.EraseClickedHandler)

    def CopyClickedHandler(self):
        QMessageBox.about(self, "The message copied is:", self.objectMyLineEdit.text())

    def EraseClickedHandler(self):
        reponseButton = QMessageBox.question(
            self,
            "Question?",
            "Confirm to erase the message?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No,
        )
        if reponseButton == QMessageBox.Yes:
            self.objectMyLineEdit.clear()
            print("Message deleted!")
        else:
            self.objectMyLineEdit.setText("Retry?")
