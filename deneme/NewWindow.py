from PyQt6.QtWidgets import *
import sys


class AnotherWindow(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        self.label = QLabel("Another Window")
        layout.addWidget(self.label)
        self.setLayout(layout)


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.button = QPushButton("Push for window")
        self.button.clicked.connect(self.show_new_window)
        self.setCentralWidget(self.button)


    def show_new_window(self, checked):
        self.w = AnotherWindow() #self ile w değişkeni yok olmuyor.
        self.w.show()


app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()
