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
start = (0, 0)
end = (0, 0)
is_down = False
rectangles = []

while not done:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if quit_operation(event):
            done = True
        if event.type == pygame.MOUSEBUTTONUP:
            end = pygame.mouse.get_pos()

            print(end)
            print(start)

            start_x, start_y = start
            end_x, end_y = end
            x1, y1 = (min(start_x, end_x), min(start_y, end_y))
            x2, y2 = (max(start_x, end_x), max(start_y, end_y))
            answer = ((x1, y1), (x2, y2))
            print(answer)
            rectangles.append(answer)
            # print(re)
            is_down = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            is_down = True
            start = pygame.mouse.get_pos()

    # if is_down:
    for i in rectangles:
        pygame.draw.rect(screen, color, i)

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
