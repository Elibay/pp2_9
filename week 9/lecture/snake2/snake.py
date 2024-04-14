import pygame

from snake2.game import Game, Point


class Snake(Game):

    def __init__(self, points, color, box_size):
        super().__init__(points, color, box_size)
        self.dir_x = 0
        self.dir_y = 1

    def change_direction(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                self.dir_x = -1
                self.dir_y = 0
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                self.dir_x = 1
                self.dir_y = 0
            if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                self.dir_x = 0
                self.dir_y = -1
            if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                self.dir_x = 0
                self.dir_y = 1

    def move(self, events):
        self.change_direction(events)
        old_point = self.get_first_point()
        new_point = Point(old_point.x + self.dir_x,
                          old_point.y + self.dir_y)
        self.points.insert(0, new_point)
        self.points.pop()

    def eat(self):
        self.points.append(self.get_first_point())


