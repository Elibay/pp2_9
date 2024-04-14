import pygame

pygame.init()
screen = pygame.display.set_mode((900, 360))
background = pygame.image.load("./images/animation/wall.jpeg")

right = [
    pygame.image.load("./images/animation/r1.png"),
    pygame.image.load("./images/animation/r2.png"),
    pygame.image.load("./images/animation/r3.png"),
    pygame.image.load("./images/animation/r4.png"),
]
left = [
    pygame.image.load("./images/animation/l1.png"),
    pygame.image.load("./images/animation/l2.png"),
    pygame.image.load("./images/animation/l3.png"),
    pygame.image.load("./images/animation/l4.png"),
]

clock = pygame.time.Clock()
x, y = (100, 220)
counter = 0
background_pos = 0

done = False
jump = False
is_still_pressed = False
jump_direction = -10
direction = left
direction_move = 10

while not done:
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            jump = True

        if event.type == pygame.KEYUP and event.key != pygame.K_SPACE:
            is_still_pressed = False

        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            direction = right
            direction_move = -10
            is_still_pressed = True

        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            direction = left
            direction_move = 10
            is_still_pressed = True

    # if is_still_pressed:
    x += direction_move
    if not jump:
        counter += 1
    if x >= 450:
        x -= 10
        background_pos += -10
    elif x <= 0:
        x = 0
        background_pos += 10

    if background_pos <= -900:
        background_pos = 0
    if jump:
        y += jump_direction
        if y < 180:
            jump_direction = 10
        if y == 220:
            jump = False
            jump_direction = -10

    screen.blit(background, (background_pos, 0))
    screen.blit(background, (background_pos + 900, 0))
    screen.blit(direction[counter % 4], (x, y))
    clock.tick(10)

print("Finished")
