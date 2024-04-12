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


def draw_line(iterations, start, end):
    color = (255, 255, 255)
    width = 2
    for i in range(iterations):
        progress = 1.0 * i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        pygame.draw.circle(screen, color, (x, y), width)


def draw(start, end):
    x, y = start
    x1, y1 = end

    color = (255, 255, 255)
    width = abs(x - x1)
    length = abs(y - y1)
    start_x = min(x, x1)
    start_y = min(y, y1)
    end = (width, length)
    pygame.draw.rect(screen, color, ((start_x, start_y), end), 1)
    # draw_line(iteration, start, end)


star_point = None
need_to_draw = False
rectangles = []

while not done:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if quit_operation(event):
            done = True

        if event.type == pygame.MOUSEMOTION:
            if need_to_draw:
                x, y = pygame.mouse.get_pos()
                if star_point:
                    draw(star_point, (x, y))

        if event.type == pygame.MOUSEBUTTONUP:
            need_to_draw = False
            x, y = pygame.mouse.get_pos()
            rectangles.append((star_point, (x, y)))

        if event.type == pygame.MOUSEBUTTONDOWN:
            need_to_draw = True
            star_point = pygame.mouse.get_pos()


    for i in rectangles:
        start, end = i
        draw(start, end)

    pygame.display.flip()

    clock.tick(60)

print("Finished")
