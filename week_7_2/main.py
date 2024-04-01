import pygame

pygame.init()

screen = pygame.display.set_mode((1300, 500))
icon = pygame.image.load("images/icon.png")
gun = pygame.image.load("images/gun.png")
gun = pygame.transform.scale(gun, (100, 100))
ball = pygame.image.load("images/ball.png")
ball = pygame.transform.scale(ball, (20, 20))
pygame.display.set_icon(icon)
pygame.display.set_caption("PP2 Game")

done = False
start_coordinates = (100, 270)

bullets = []


counter = 0
while not done:
    counter += 1
    if counter % 20 == 0:
        # moving
        new_array = []
        for bullet in bullets:
            x, y = bullet
            new_array.append((x + 10, y))
        bullets = new_array

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            bullets.append(start_coordinates)

    screen.fill((0, 0, 0))
    screen.blit(gun, (0, 250))

    for bullet in bullets:
        screen.blit(ball, bullet)

print("Finished")

