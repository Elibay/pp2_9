import random

import pygame

from db_util import get_students, add_student_to_db, remove_student_from_db, get_average

pygame.init()
screen = pygame.display.set_mode((400, 600))
done = False

clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)
green_color = (105, 245, 66)
red_color = (240, 10, 29)


def print_buttons():
    pygame.draw.rect(screen, green_color, (150, 10, 40, 40))
    pygame.draw.rect(screen, red_color, (200, 10, 40, 40))


def is_plus_button(x, y):
    if x >= 150 and x <= 190 and y >= 10 and y <= 50:
        return True
    return False


def is_minus_button(x, y):
    if x >= 200 and x <= 240 and y >= 10 and y <= 50:
        return True
    return False


def add_student():
    grade = random.randint(1, 5)
    student = "ABCBBCBCB"

    add_student_to_db(grade, student)


def remove_student():
    remove_student_from_db()


def print_students(students):
    x, y = 40, 60
    for student in students:
        id, grade, full_name = student
        text = f"{id}, {grade}, {full_name}"
        text_render = font.render(text, True, (0, 0, 0))

        screen.blit(text_render, (x, y))
        y += 30


def print_average():
    text = "%.2f" % get_average()[0]
    text_render = font.render(text, True, (0, 0, 0))

    screen.blit(text_render, (260, 20))


while not done:
    pygame.display.update()
    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            if is_minus_button(x, y):
                remove_student()
            if is_plus_button(x, y):
                add_student()

    students = get_students()
    print_students(students)
    print_average()
    print_buttons()

print("Finished")
