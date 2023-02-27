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
    mainmenu._open(loading)
    pygame.time.set_timer(update_loading, 30)


def level_menu():
    mainmenu._open(level)


mainmenu = pygame_menu.Menu('САПЁР', 600, 400, theme=themes.THEME_SOLARIZED)
mainmenu.add.text_input('Введите никнейм: ', default='новый_игрок')
mainmenu.add.button('Играть', start_the_game)
mainmenu.add.button('Уровни', level_menu)
mainmenu.add.button('Выход из игры', pygame_menu.events.EXIT)

level = pygame_menu.Menu('Select a Difficulty', 600, 400, theme=themes.THEME_BLUE)
level.add.selector('Сложность :', [('Сложно', 1), ('Легко', 2)], onchange=set_difficulty)

loading = pygame_menu.Menu('Загрузка игры...', 600, 400, theme=themes.THEME_DARK)

update_loading = pygame.USEREVENT + 0

while True:
    events = pygame.event.get()
    for event in events:
        if event.type == update_loading:
            progress = loading.get_widget("1")
            progress.set_value(progress.get_value() + 1)
            if progress.get_value() == 100:
                pygame.time.set_timer(update_loading, 0)
        if event.type == pygame.QUIT:
            exit()

    if mainmenu.is_enabled():
        mainmenu.update(events)
        mainmenu.draw(surface)

    pygame.display.update()
