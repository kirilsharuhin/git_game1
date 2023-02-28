import pygame
import pygame_menu
from pygame_menu import themes

pygame.init()
window = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Сапёр")
pygame.mixer.music.load("data/fon_music.mp3")
pygame.mixer.music.play(-1)


def set_difficulty(value, difficulty):
    print(value)
    print(difficulty)


def start_the_game():
    from main import new_game
    mainmenu._open(new_game)


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

level = pygame_menu.Menu('Все уровни генерируются', 600, 400, theme=themes.THEME_BLUE)
level.add.selector('Сложность :', [('Как повезёт', 1), ('Как повезёт', 2)], onchange=set_difficulty)

pravila = pygame_menu.Menu('Об игре и её правила', 600, 400, theme=themes.THEME_BLUE)
pravila.add.text_input("Невежда так же в ослепленье")
pravila.add.text_input("Невежда так же в ослепленье")
pravila.add.text_input("Невежда так же в ослепленье")
pravila.add.text_input("Невежда так же в ослепленье")
pravila.add.text_input("Невежда так же в ослепленье")
pravila.add.text_input("нужно как то нормально выводить простой текст(")


while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            exit()

    if mainmenu.is_enabled():
        mainmenu.update(events)
        mainmenu.draw(window)

    pygame.display.update()
