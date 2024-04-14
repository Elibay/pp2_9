from snake.game import Game


class Food(Game):

    def can_eat(self, point):
        print(point)
        print(self.get_first_point())
        if point == self.get_first_point():
            return True
        return False
