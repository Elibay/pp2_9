import random

import pygame


def load_rocket():
    r = pygame.image.load("../images/rocket.png")
    r = pygame.transform.scale(r, (50, 50))

    return r


def get_random_place(l, r):
    return (random.randint(l, r), 0)


def load_earth():
    r = pygame.image.load("../images/moon.png")
    r = pygame.transform.scale(r, (50, 50))

    return r


def get_earth_coordinates(counter):
    result = []
    for i in range(counter):
        if i % 2 == 0:
            result.append(get_random_place(0, 500))
        else:
            result.append(get_random_place(500, 1000))

    return result


def set_icon():
    # icon = pygame.image.load("images/icon2.png")
    icon = pygame.image.load("../images/icon2.png")
    pygame.display.set_icon(icon)
    pygame.display.set_caption("PP2")


def get_init_coordinates():
    return (450, 440)


pygame.init()
screen = pygame.display.set_mode((900, 500))
set_icon()
rocket = load_rocket()
x, y = get_init_coordinates()
earth = load_earth()
earth_coordinates = get_earth_coordinates(6)
clock = pygame.time.Clock()

done = False

counter = 0
while not done:
    counter += 1
    pygame.display.update()
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_d:
            x += 10
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_a:
            x -= 10

    # pygame.draw.rect(screen, background, pygame.Rect(x, y, 60, 60))
    # pygame.display.flip()
    for coordinate in earth_coordinates:
        screen.blit(earth, coordinate)

    if counter % 100 == 0:
        new_array = []
        for coordinate in earth_coordinates:
            new_x, new_y = coordinate
            new_array.append((new_x, new_y + 10))
        earth_coordinates = new_array

    screen.blit(rocket, (x, y))
    # clock.tick(60)

print("Finished")
