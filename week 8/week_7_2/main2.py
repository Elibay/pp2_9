import pygame

pygame.init()

screen = pygame.display.set_mode((1300, 500))
icon = pygame.image.load("images/icon.png")
gun = pygame.image.load("images/gun.png")
ball = pygame.image.load("images/ball.png")
pygame.display.set_icon(icon)
pygame.display.set_caption("PP2 Game")

red = (252, 5, 5)
blue = (20, 156, 247)

background = red

done = False

x = 650
y = 250

while not done:
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            background = blue
        elif event.type == pygame.KEYDOWN:
            background = red

        if event.type == pygame.KEYDOWN and event.key == pygame.K_a:
            x -= 10
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_d:
            x += 10
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_w:
            y -= 10
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_s:
            y += 10

    screen.fill((0, 0, 0))
    # pygame.draw.circle(screen, background, (650, 250), 50)
    pygame.draw.rect(screen, background, (x, y, 50, 50), width=1)



print("Finished")

