import sys

from food_gui import MyWindow
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication


def main():
    app = QApplication(sys.argv)
    window = MyWindow()
    window.setWindowIcon(QIcon("meal-food-icon.png"))
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
