from snake2.game import Game, Point


class Wall(Game):

    def __init__(self, color, box_size):
        super().__init__(self.read_wall(), color, box_size)
        self.level = 0
        print(self.points)

    def read_wall(self):
        f = open("../levels/level0.txt", "r")
        x = 0
        points = []
        for row in f:
            y = 0
            for column in row:
                if column == '#':
                    points.append(Point(y, x))
                y += 1
            x += 1

        return points
