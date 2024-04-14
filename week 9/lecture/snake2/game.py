import pygame.draw


class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"x: {self.x}, y: {self.y}"

    def __eq__(self, other):
        if other.x == self.x and other.y == self.y:
            return True
        return False


class Game():

    def __init__(self, points, color, box_size):
        self.points = points
        self.color = color
        self.box_size = box_size

    def draw(self, screen):
        for point in self.points:
            pygame.draw.rect(screen, self.color, (point.x * self.box_size, point.y * self.box_size, self.box_size,
                             self.box_size))

    def get_first_point(self):
        return self.points[0]
