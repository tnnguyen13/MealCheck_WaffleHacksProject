import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QInputDialog, QLineEdit


class MainWindow(QtWidgets.QWidget):
    """Represents the main gui window."""
    def __init__(self):
        super().__init__()
        self.title = 'Your Search Results'
        self.restaurant = QtWidgets.QLabel("This is the closest restaurant to you: ", self)
        self.rating = QtWidgets.QLabel("Current Rating: ", self)
        self.reviews = QtWidgets.QLabel("Number of reviews: ", self)
        self.price = QtWidgets.QLabel("Price Rating:", self)
        self.initUI()

    def initUI(self):
        """Initializes the widgets in the window.
        These widgets will be updated by methods later methods in the class."""

        self.setWindowTitle(self.title)
        self.setLayout(QtWidgets.QVBoxLayout())

        self.layout().addWidget(self.restaurant)
        self.layout().addWidget(self.rating)
        self.layout().addWidget(self.reviews)
        self.layout().addWidget(self.price)

        self.show()

    def get_name(self):
        """Gets a name from user input."""
        text, ok_pressed = QInputDialog.getText(self, "Get name", "Your name:", QLineEdit.Normal, "")
        if ok_pressed and text != '':
            return text

    def get_food(self):
        """Gets a food search from the user."""
        text, ok_pressed = QInputDialog.getText(self, "Get food", "What type of food do you want?", QLineEdit.Normal, "")
        if ok_pressed and text != '':
            return text

    def get_zip(self):
        """Obtains the user's zipcode."""
        text, ok_pressed = QInputDialog.getText(self, "Get zipcode", "What's your zipcode?", QLineEdit.Normal, "")
        if ok_pressed and text != '':
            return text

    def update_data(self, widget, text):
        """Updates the data in the specified widget with the specified extra text."""
        widget.setText(f'{widget.text()} {text}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())

