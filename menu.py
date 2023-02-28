from time import sleep
import pygame
import pygame_menu
from pygame_menu import themes

pygame.init()
surface = pygame.display.set_mode((600, 400))


def set_difficulty(value, difficulty):
    print(value)
    print(difficulty)


def start_the_game():
    pass


def level_menu():
    mainmenu._open(level)


def pravila_menu():
    mainmenu._open(pravila)


mainmenu = pygame_menu.Menu('САПЁР', 600, 400, theme=themes.THEME_SOLARIZED)
mainmenu.add.text_input('Введите никнейм: ', default='unknown')
mainmenu.add.button('Играть', start_the_game)
mainmenu.add.button('Уровни', level_menu)
mainmenu.add.button('Об игре и её правила', pravila_menu)
mainmenu.add.button('Выход из игры', pygame_menu.events.EXIT)

level = pygame_menu.Menu('Выберите сложность: ', 600, 400, theme=themes.THEME_BLUE)
level.add.selector('Сложность :', [('Сложно', 1), ('Легко', 2)], onchange=set_difficulty)

pravila = pygame_menu.Menu('Об игре и её правила', 600, 400, theme=themes.THEME_BLUE)
pravila.add.text('igyu')


while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            exit()

    if mainmenu.is_enabled():
        mainmenu.update(events)
        mainmenu.draw(surface)

    pygame.display.update()
