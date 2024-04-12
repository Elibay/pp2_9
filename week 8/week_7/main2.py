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


color = (250, 245, 245)
points = []
width = 2
is_down = False
pressed = []


def draw_line(iterations, start, end, color, width):
    for i in range(iterations):
        progress = 1.0 * i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        pygame.draw.circle(screen, color, (x, y), width)


def draw_points(points):
    for i in range(len(points) - 1):
        x, y = points[i]
        x2, y2 = points[i + 1]
        x_max = abs(x - x2)
        y_max = abs(y - y2)
        iterations = max(x_max, y_max)

        draw_line(iterations, points[i], points[i + 1], color, width)


while not done:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if quit_operation(event):
            done = True
        if event.type == pygame.MOUSEMOTION:
            if is_down == True:
                points.append(pygame.mouse.get_pos())
        if event.type == pygame.MOUSEBUTTONUP:
            pressed.append(points)
            points = []
            is_down = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            is_down = True

        if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
            width = min(width + 1, 100)

        if event.type == pygame.KEYDOWN and event.key == pygame.K_m:
            width = max(width - 1, 2)

    for i in pressed:
        draw_points(i)
    draw_points(points)

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
