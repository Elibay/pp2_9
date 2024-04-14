import pygame

from snake2.food import Food
from snake2.game import Point
from snake2.snake import Snake
from snake2.wall import Wall


def create_background(screen, width, height):
    colors = [(255, 255, 255), (150, 146, 135)]
    box_size = 20
    row = 0
    while row <= width:
        column = 0
        while column <= height:
            x = row // box_size + column // box_size
            pygame.draw.rect(screen, colors[x % 2], (row, column, box_size, box_size))
            column += box_size
        row += box_size


done = False

pygame.init()
screen = pygame.display.set_mode((400, 320))
clock = pygame.time.Clock()

wall = Wall(color=(242, 5, 13), box_size=20)
food = Food(points=[Point(1, 1)], color=(215, 245, 66), box_size=20)
snake = Snake(points=[Point(2, 2)], color=(40, 252, 8), box_size=20)

while not done:
    # Event filtering
    filtered_events = []
    create_background(screen, 400, 300)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        else:
            filtered_events.append(event)

    if food.can_eat(snake.get_first_point()):
        snake.eat()
        food.change_location()

    snake.move(events=filtered_events)

    food.draw(screen)
    wall.draw(screen)
    snake.draw(screen)

    pygame.display.flip()
    clock.tick(5)
