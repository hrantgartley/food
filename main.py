from sys import argv, exit

from food_gui import MyWindow
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication


def main():
    app = QApplication(argv)
    window = MyWindow()
    window.setWindowIcon(QIcon("food-meal-icon.png"))
    window.show()
    exit(app.exec_())


if __name__ == "__main__":
    main()