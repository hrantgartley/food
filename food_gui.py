import random
import sys
from datetime import datetime
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton
from PyQt5.QtGui import QIcon


class WeekdayFood:
    def __init__(self):
        self.choice = [
            "Chick-fil-A",
            "Moe's",
            "Panda Express",
            "Cafeteria",
            "Burger 256",
            "CREATE",
            "Lions Corner",
        ]
        self.rand_index = random.randint(0, len(self.choice) - 1)

    def get_food(self):
        weekday_food = random.choice(self.choice)
        return weekday_food

    def __str__(self):
        return f"Weekday food: {self.get_food()}"


class WeekendFood(WeekdayFood):
    def __init__(self):
        self.choice = ["Chick-fil-A", "Cafeteria", "CREATE", "Starbucks"]
        self.rand_index = random.randint(0, len(self.choice) - 1)

    def __str__(self):
        return f"Weekend food: {self.get_food()}"


class HomeFood(WeekdayFood):
    def __init__(self):
        with open("food.txt", "r") as f:
            self.choice = [line.splitlines() for line in f.readlines()]
        self.rand_index = random.randint(0, len(self.choice) - 1)

    def __str__(self):
        food_item = self.get_food()
        return f'Home food: {", ".join(food_item)}'


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 400, 200)
        self.setWindowTitle("Food Picker for UNA")
        self.label = QLabel(self)
        self.label.move(100, 20)
        self.label.setGeometry(150, 20, 200, 50)
        self.label.setText("FOOD PICKER")

        self.button = QPushButton(self)
        self.button.move(150, 80)
        self.button.setText("Get Food")
        self.button.clicked.connect(self.display_food)

    def display_food(self):
        current_month = datetime.today().month

        if current_month >= 5 and current_month <= 7:
            home_food = HomeFood()
            self.label.setText(str(home_food))
        # checks if it's a weekday and if the month is between august and april
        elif (
            datetime.today().weekday() < 5 and current_month >= 8 and current_month <= 4
        ):
            weekday_food = WeekdayFood()
            self.label.setText(str(weekday_food))
        # it's a weekend and if the month is between august and april
        else:
            weekend_food = WeekendFood()
            self.label.setText(str(weekend_food))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.setWindowIcon(QIcon("meal-food-icon.png"))
    window.show()
    sys.exit(app.exec_())
