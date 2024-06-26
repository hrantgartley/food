import random
from datetime import datetime

from PyQt5.QtWidgets import QLabel, QMainWindow, QPushButton


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
            "Cafe Dallucci",
        ]
        self.rand_index = random.randint(0, len(self.choice) - 1)

    def get_food(self):
        weekday_food = random.choice(self.choice)
        return weekday_food

    def __str__(self):
        return f"Weekday food: {self.get_food()}"


class WeekendFood(WeekdayFood):
    def __init__(self):
        super().__init__()
        self.choice = ["Chick-fil-A", "Cafeteria", "CREATE", "Starbucks"]
        self.rand_index = random.randint(0, len(self.choice) - 1)

    def __str__(self):
        return f"Weekend food: {self.get_food()}"


class HomeFood(WeekdayFood):
    def __init__(self):
        super().__init__()
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
        self.label.setText("FOOD SELECTOR")

        self.button = QPushButton(self)
        self.button.move(150, 80)
        self.button.setText("Get Food")
        self.button.clicked.connect(self.display_food)

    def display_food(self):
        current_month = datetime.today().month

        if 5 <= current_month <= 7:
            home_food = HomeFood()
            self.label.setText(str(home_food))

        elif (
                datetime.today().weekday() < 5 and 8 <= current_month <= 4
        ):
            weekday_food = WeekdayFood()
            self.label.setText(str(weekday_food))

        elif datetime.today().weekday() == 6 and 8 <= current_month <= 4:
            weekend_food = WeekendFood()
            weekend_food.choice.remove("Chick-fil-A")
            self.label.setText(str(weekend_food))

        else:
            weekend_food = WeekendFood()
            self.label.setText(str(weekend_food))
