import math

import pygame

pygame.init()
screen = pygame.display.set_mode((900, 500))
clock = pygame.time.Clock()

done = False


def quit_operation(event):
    if event.type == pygame.QUIT:
        return True
    if event.type == pygame.KEYDOWN and (event.key == pygame.K_LALT or event.key == pygame.K_RALT):
        return True
    if event.type == pygame.KEYDOWN and (event.key == pygame.K_RCTRL or event.key == pygame.K_LCTRL):
        return True
    if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
        return True
    return False


star_point = None
need_to_draw = False
rectangles = []
color = (52, 235, 67)
center = (450, 250)


def draw_circle(width, direction):
    width += direction
    if width > 200:
        direction = -4
    if width < 10:
        direction = 4

    pygame.draw.circle(screen, color, center, width)
    return width, direction


def rotate_point_around_center(x, y, cx, cy, theta):
    # Translate the point so that the center of rotation is at the origin
    x_translated = x - cx
    y_translated = y - cy

    # Convert angle from degrees to radians
    theta = math.radians(theta)

    # Perform the rotation
    x_rotated = x_translated * math.cos(theta) - y_translated * math.sin(theta)
    y_rotated = x_translated * math.sin(theta) + y_translated * math.cos(theta)

    # Translate the point back to its original position
    x_final = x_rotated + cx
    y_final = y_rotated + cy

    return x_final, y_final


def draw_star(direction):
    x, y = (450, 250)
    sides = 5
    points = []
    k = 100
    pi = 3.1415
    for i in range(sides * 2):
        x, y = center
        r = k
        if i % 2 == 0:
            r = k / 2.0
        x1 = x + r * 1.0 * math.cos(2 * pi * i * 1.0 / 5 + pi / 2)  # formula from internet
        y1 = y + r * 1.0 * math.sin(2 * pi * i / 5 + pi / 2)
        points.append((int(x1), int(y1)))

    # pygame.draw.polygon(screen, color, points)

    for i in range(len(points)):
        x, y = points[i]
        points[i] = rotate_point_around_center(x, y, 450, 250, direction)

    pygame.draw.polygon(screen, color, points)
    pygame.draw.circle(screen, color, (450, 250), k / 2 + 3)

    return points


d = 0
while not done:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if quit_operation(event):
            done = True

    d += 1
    points = draw_star(d)

    # x, y = draw_circle(x, y)

    pygame.display.flip()

    clock.tick(60)

print("Finished")
