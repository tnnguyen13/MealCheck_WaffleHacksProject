import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QInputDialog, QLineEdit


class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Your Search Results'
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setLayout(QtWidgets.QVBoxLayout())
        self.restaurant = QtWidgets.QLabel("This is the closest restaurant to you: ", self)
        self.layout().addWidget(self.restaurant)
        self.rating = QtWidgets.QLabel("Current Rating: ", self)
        self.layout().addWidget(self.rating)
        self.reviews = QtWidgets.QLabel("Number of reviews: ", self)
        self.layout().addWidget(self.reviews)
        self.price = QtWidgets.QLabel("Price Rating:", self)
        self.layout().addWidget(self.price)
        self.show()

    def get_name(self):
        text, ok_pressed = QInputDialog.getText(self, "Get text", "Your name:", QLineEdit.Normal, "")
        if ok_pressed and text != '':
            return text

    def get_food(self):
        text, ok_pressed = QInputDialog.getText(self, "Get text", "What type of food do you want?", QLineEdit.Normal, "")
        if ok_pressed and text != '':
            return text

    def get_zip(self):
        text, ok_pressed = QInputDialog.getText(self, "Get text", "What's your zipcode?", QLineEdit.Normal, "")
        if ok_pressed and text != '':
            return text

    def update_data(self, widget, text):
        widget.setText(f'{widget.text()} {text}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())

