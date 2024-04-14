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

done = False

counter = 0
background_pos = 0
x = 100
y = 220
jump = False
jump_speed = 10
direction = -1 * jump_speed

player_direction = left

while not done:
    pygame.display.update()
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            jump = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            counter += 1
            player_direction = right
            x -= 5
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            player_direction = left
            counter += 1
            x += 5

    # background_pos -= 5
    # if background_pos <= -900:
    #     background_pos = 0

    if jump:
        y += direction
        if y <= 150:
            direction = 1 * jump_speed
        if y == 220:
            jump = False
            direction = -1 * jump_speed
    # else:
    #     counter += 1

    screen.blit(background, (background_pos + 0, 0))
    # screen.blit(background, (background_pos + 900, 0))
    screen.blit(player_direction[counter % 4], (x, y))
    clock.tick(10)

print("Finished")
