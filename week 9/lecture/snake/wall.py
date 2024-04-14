from snake.game import Game, Point


class Wall(Game):

    def __init__(self, box_size, color):
        super().__init__(self.get_points(), box_size, color)
        self.level = 0

    def get_points(self):
        f = open("../levels/level0.txt", "r")
        points = []
        x = 0
        for row in f:
            y = 0
            for column in row:
                if column == '#':
                    points.append(Point(x, y))
                y += 1
            x += 1
        return points
