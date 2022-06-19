import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QInputDialog, QLineEdit


class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Search for Food'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

    def get_name(self):
        text, ok_pressed = QInputDialog.getText(self, "Get text", "Your name:", QLineEdit.Normal, "")
        if ok_pressed and text != '':
            return text

    def get_food(self):
        text, ok_pressed = QInputDialog.getText(self, "Get text", "What type of food do you want?", QLineEdit.Normal, "")
        if ok_pressed and text != '':
            return text

    def get_zip(self):
        i, ok_pressed = QInputDialog.getInt(self, "Get integer", "What's your zipcode?", 00000, 0, 99999, 1)
        if ok_pressed:
            return i


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())

