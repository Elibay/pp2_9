import pygame

from db_utils import select_all_data_from_table, add_data_to_table, remove_data_from_table

pygame.init()
screen = pygame.display.set_mode((400, 600))
done = False

clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)
green_color = (105, 245, 66)
red_color = (240, 10, 29)


def print_users_table():
    users = select_all_data_from_table()
    response = []
    for user in users:
        id, phone_number, name = user
        text = f"{id} {phone_number} {name}"
        text_render = font.render(text, True, (0, 0, 0))
        response.append(text_render)
    return response


def plus_button_clicked_check(x, y):
    if x >= 150 and x <= 190 and y >= 10 and y <= 50:
        return True
    return False


def minus_button_clicked_check(x, y):
    if x >= 200 and x <= 240 and y >= 10 and y <= 50:
        return True
    return False


def add_data_string():
    phone_number = "+77770707177"
    name = "ABCBBC"
    add_data_to_table(phone_number, name)


def delete_last_data():
    remove_data_from_table()



while not done:
    pygame.display.update()
    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            if plus_button_clicked_check(x, y):
                add_data_string()
            elif minus_button_clicked_check(x, y):
                delete_last_data()
    x = 50
    y = 60

    pygame.draw.rect(screen, green_color, (150, 10, 40, 40))
    pygame.draw.rect(screen, red_color, (200, 10, 40, 40))
    users = print_users_table()

    for user in users:
        screen.blit(user,
                    (x, y))
        y += 50

    clock.tick(10)

print("Finished")
