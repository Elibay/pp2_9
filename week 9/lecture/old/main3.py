import math

import pygame

pygame.init()
screen = pygame.display.set_mode((900, 500))
center = (450, 250)
clock = pygame.time.Clock()

done = False

color = (252, 3, 3)


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


counter_main = 10
direction_main = 5
k = 200
pi = 3.1415


def draw_circle(counter, direction):
    counter += direction
    if counter > 200:
        direction = -5
    if counter <= 10:
        direction = 5
    pygame.draw.circle(screen, color, center, counter / 2)
    return counter, direction

def draw_star():
    x, y = (450, 250)
    sides = 5
    points = []
    r = k
    # for i in range(sides * 2):
    #     if i % 2 == 0:
    #         r = k // 2
    #     ang = i * 3.14159 / sides + 3.14159 / 60
    #     x1 = x + int(math.cos(ang) * r)
    #     y1 = y + int(math.sin(ang) * r)
    #     points.append((x1, y1))

    for i in range(sides * 2):
        x, y = center
        r = k
        if i % 2 == 0:
            r = k / 2.0
        x1 = x + r * 1.0 * math.cos(2 * pi * i * 1.0 / 5 + pi / 2)  # formula from internet
        y1 = y + r * 1.0 * math.sin(2 * pi * i / 5 + pi / 2)
        points.append((int(x1), int(y1)))

    print(points)

    return points


screen.fill((250, 245, 245))
points = draw_star()


while not done:

    for event in pygame.event.get():
        if quit_operation(event):
            done = True

    # counter_main, direction_main = draw_circle(counter_main, direction_main)
    # sides = 5

    pygame.draw.polygon(screen, color, points)
    pygame.display.flip()

    clock.tick(60)

print("Finished")

#
#
#
#
# def rotate_3d_points(points, angle_x, angle_y, angle_z):
#     new_points = []
#     for point in points:
#         x = point[0]
#         y = point[1]
#         z = point[2]
#         new_y = y * math.cos(angle_x) - z * math.sin(angle_x)
#         new_z = y * math.sin(angle_x) + z * math.cos(angle_x)
#         y = new_y
#         # isn't math fun, kids?
#         z = new_z
#         new_x = x * math.cos(angle_y) - z * math.sin(angle_y)
#         new_z = x * math.sin(angle_y) + z * math.cos(angle_y)
#         x = new_x
#         z = new_z
#         new_x = x * math.cos(angle_z) - y * math.sin(angle_z)
#         new_y = x * math.sin(angle_z) + y * math.cos(angle_z)
#         x = new_x
#         y = new_y
#         new_points.append([x, y, z])
#     return new_points
