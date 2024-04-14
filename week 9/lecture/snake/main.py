import pygame

from snake.food import Food
from snake.game import Point
from snake.snak import Snake
from snake.wall import Wall


def create_background(screen, width, height):
    colors = [(255, 255, 255), (150, 146, 135)]
    box_size = 20
    l = 0
    while l <= width:
        r = 0
        while r <= height:
            x = l // box_size + r // box_size
            pygame.draw.rect(screen, colors[x % 2], (l, r, box_size, box_size))
            r += box_size
        l += box_size


done = False

pygame.init()
screen = pygame.display.set_mode((400, 320))
clock = pygame.time.Clock()

box_size = 20

food = Food(points=[Point(3, 2)], box_size=box_size, color=(252, 186, 3))
wall = Wall(box_size=box_size, color=(227, 9, 38))
snake = Snake(points=[Point(1, 1)], box_size=box_size, color=(6, 114, 153))


while not done:
    # Event filtering
    filtered_events = []
    create_background(screen, 400, 300)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        else:
            filtered_events.append(event)

    snake.move(filtered_events)
    if food.can_eat(snake.get_first_point()):
        print("i am here")
        snake.eat()

    food.draw(screen)
    # wall.draw(screen)
    snake.draw(screen)
    pygame.display.flip()
    clock.tick(5)
