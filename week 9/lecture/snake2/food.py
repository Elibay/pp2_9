import random

from snake2.game import Game, Point


class Food(Game):
    def can_eat(self, point):
        if self.get_first_point() == point:
            return True
        return False

    def change_location(self):
        x = random.randrange(0, 19)
        y = random.randrange(0, 15)
        new_point = Point(x, y)
        self.points.pop()
        self.points.append(new_point)
