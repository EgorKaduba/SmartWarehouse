from idlelib.run import exit_now
import pygame
from pygame import Color
import sys

fps = 150

win_width = 1600
win_height = 800

white = (255, 255, 255)
orange = (255, 150, 100)
black = (0, 0, 0)

clock = pygame.time.Clock()


def message(sc, font_style, msg, color, x, y):
    msg = str(msg)
    mesg = font_style.render(msg, True, color)
    sc.blit(mesg, (x, y))


def get_from_db(packs, new_pack=None):
    pygame.init()
    font_style = pygame.font.Font('my_font.ttf', 24)
    sc = pygame.display.set_mode((win_width, win_height))
    flag = True
    flag2 = True
    y_now = 0
    x_now = 0
    while 1:
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                pygame.quit()
                return
        # заливаем фон
        sc.fill(white)

        pygame.draw.rect(sc, black, pygame.Rect(370, 720, 15, 15), 2)
        pygame.draw.rect(sc, orange, pygame.Rect(372, 722, 11, 11))
        message(sc, font_style, "Лента загрузки/выгрузки", black, 390, 710)

        pygame.draw.rect(sc, Color(34, 82, 17), pygame.Rect(370, 760, 15, 15), 2)
        pygame.draw.rect(sc, Color(62, 173, 23), pygame.Rect(372, 762, 11, 11))
        message(sc, font_style, "Лента хранения", black, 390, 750)

        pygame.draw.rect(sc, Color(34, 82, 17), pygame.Rect(730, 720, 15, 15), 2)
        pygame.draw.rect(sc, Color(176, 189, 172), pygame.Rect(732, 722, 11, 11))
        message(sc, font_style, "Лента транспортировки", black, 750, 710)

        pygame.draw.rect(sc, Color(34, 82, 17), pygame.Rect(730, 760, 15, 15), 2)
        pygame.draw.rect(sc, Color(199, 119, 28), pygame.Rect(732, 762, 11, 11))
        message(sc, font_style, "Коробка", black, 750, 750)

        pygame.draw.rect(sc, Color(34, 82, 17), pygame.Rect(930, 760, 15, 15), 2)
        pygame.draw.rect(sc, Color("red"), pygame.Rect(932, 762, 11, 11))
        message(sc, font_style, "Сканер", black, 950, 750)

        for ver in range(45):
            for gor in range(10):
                x1, y1 = 50 + gor * 17, 775 - ver * 17
                pygame.draw.rect(sc, black, pygame.Rect(x1, y1, 15, 15), 2)
                pygame.draw.rect(sc, orange, pygame.Rect(x1 + 2, y1 + 2, 11, 11))
        color = Color(62, 173, 23)
        i = 0
        for ver in range(5, 45):
            if i % 10 == 0:
                color = Color(176, 189, 172) if color.r == 62 else Color(62, 173, 23)
            i += 1
            for gor in range(10, 75):
                x1, y1 = 50 + gor * 17, 775 - ver * 17
                pygame.draw.rect(sc, Color(34, 82, 17), pygame.Rect(x1, y1, 15, 15), 2)
                pygame.draw.rect(sc, color, pygame.Rect(x1 + 2, y1 + 2, 11, 11))
        for ver in range(45):
            for gor in range(75, 85):
                x1, y1 = 50 + gor * 17, 775 - ver * 17
                pygame.draw.rect(sc, black, pygame.Rect(x1, y1, 15, 15), 2)
                pygame.draw.rect(sc, orange, pygame.Rect(x1 + 2, y1 + 2, 11, 11))

        for pack in packs:
            y = pack[1]
            y = (y // 10) * 10 + y
            x1 = 220 + pack[0] * 15 + pack[0] * 2
            y1 = 27 + y * 15 + y * 2
            height = 15 * pack[2] + (pack[2] - 1) * 2
            width = 15 * pack[3] + (pack[3] - 1) * 2
            pygame.draw.rect(sc, Color(199, 119, 28), pygame.Rect(x1, y1, width, height))

            y = new_pack[1]
            y = (y // 10) * 10 + y
            height = 15 * new_pack[2] + (new_pack[2] - 1) * 2
            width = 15 * new_pack[3] + (new_pack[3] - 1) * 2
            x_res = 220 + new_pack[0] * 15 + new_pack[0] * 2
            y_res = 27 + y * 15 + y * 2
            if flag:
                x_now = 218 - width
                y_now = 790 - height
                flag = False
            y_con = 197 if y < 11 else 537
            if y_now != y_con and flag2:
                y_now -= 1
            else:
                flag2 = False
                if x_now != x_res:
                    x_now += 1
                else:
                    if y_now != y_res:
                        y_now -= 1
            pygame.draw.rect(sc, Color(199, 119, 28), pygame.Rect(x_now, y_now, width, height))

        pygame.draw.rect(sc, Color("red"), pygame.Rect(215, 730, 20, 30))

        # обновляем окно
        pygame.display.update()
        clock.tick(fps)
