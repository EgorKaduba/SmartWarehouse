import pygame
from pygame import Color
import sys

fps = 140
win_width = 1600
win_height = 800
white = (255, 255, 255)
orange = (255, 150, 100)

black = (0, 0, 0)
clock = pygame.time.Clock()


# def print_warehouse():
#     sc = pygame.display.set_mode((win_width, win_height))
#     while 1:
#         for i in pygame.event.get():
#             if i.type == pygame.QUIT:
#                 pygame.quit()
#                 return
#         # заливаем фон
#         sc.fill(white)
#         for ver in range(45):
#             for gor in range(10):
#                 x1, y1 = 50 + gor * 17, 775 - ver * 17
#                 pygame.draw.rect(sc, black, pygame.Rect(x1, y1, 15, 15), 2)
#                 pygame.draw.rect(sc, orange, pygame.Rect(x1 + 2, y1 + 2, 11, 11))
#         color = Color(62, 173, 23)
#         i = 0
#         for ver in range(5, 45):
#             if i % 10 == 0:
#                 color = Color(176, 189, 172) if color.r == 62 else Color(62, 173, 23)
#             i += 1
#             for gor in range(10, 75):
#                 x1, y1 = 50 + gor * 17, 775 - ver * 17
#                 pygame.draw.rect(sc, Color(34, 82, 17), pygame.Rect(x1, y1, 15, 15), 2)
#                 pygame.draw.rect(sc, color, pygame.Rect(x1 + 2, y1 + 2, 11, 11))
#         for ver in range(45):
#             for gor in range(75, 85):
#                 x1, y1 = 50 + gor * 17, 775 - ver * 17
#                 pygame.draw.rect(sc, black, pygame.Rect(x1, y1, 15, 15), 2)
#                 pygame.draw.rect(sc, orange, pygame.Rect(x1 + 2, y1 + 2, 11, 11))
#         pygame.draw.rect(sc, orange, pygame.Rect(220, 367, 11, 11))
#
#         # обновляем окно
#         pygame.display.update()
#         clock.tick(fps)


def get_from_db(packs, new_pack=None):
    sc = pygame.display.set_mode((win_width, win_height))
    while 1:
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                pygame.quit()
                return
        # заливаем фон
        sc.fill(white)
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

        if new_pack is not None:
            y = new_pack[1]
            y = (y // 10) * 10 + y
            x1 = 220 + new_pack[0] * 15 + new_pack[0] * 2
            y1 = 27 + y * 15 + y * 2
            height = 15 * new_pack[2] + (new_pack[2] - 1) * 2
            width = 15 * new_pack[3] + (new_pack[3] - 1) * 2
            pygame.draw.rect(sc, Color(199, 119, 28), pygame.Rect(x1, y1, width, height))

        for pack in packs:
            y = pack[1]
            y = (y // 10) * 10 + y
            x1 = 220 + pack[0] * 15 + pack[0] * 2
            y1 = 27 + y * 15 + y * 2
            height = 15 * pack[2] + (pack[2] - 1) * 2
            width = 15 * pack[3] + (pack[3] - 1) * 2
            pygame.draw.rect(sc, Color(199, 119, 28), pygame.Rect(x1, y1, width, height))
        # обновляем окно
        pygame.display.update()
        clock.tick(fps)


# def add_pack(packs, new_pack):
#     sc = pygame.display.set_mode((win_width, win_height))
#     while 1:
#         for i in pygame.event.get():
#             if i.type == pygame.QUIT:
#                 pygame.quit()
#                 return
#         # заливаем фон
#         sc.fill(white)
#         for ver in range(45):
#             for gor in range(10):
#                 x1, y1 = 50 + gor * 17, 775 - ver * 17
#                 pygame.draw.rect(sc, black, pygame.Rect(x1, y1, 15, 15), 2)
#                 pygame.draw.rect(sc, orange, pygame.Rect(x1 + 2, y1 + 2, 11, 11))
#         color = Color(62, 173, 23)
#         i = 0
#         for ver in range(5, 45):
#             if i % 10 == 0:
#                 color = Color(176, 189, 172) if color.r == 62 else Color(62, 173, 23)
#             i += 1
#             for gor in range(10, 75):
#                 x1, y1 = 50 + gor * 17, 775 - ver * 17
#                 pygame.draw.rect(sc, Color(34, 82, 17), pygame.Rect(x1, y1, 15, 15), 2)
#                 pygame.draw.rect(sc, color, pygame.Rect(x1 + 2, y1 + 2, 11, 11))
#         for ver in range(45):
#             for gor in range(75, 85):
#                 x1, y1 = 50 + gor * 17, 775 - ver * 17
#                 pygame.draw.rect(sc, black, pygame.Rect(x1, y1, 15, 15), 2)
#                 pygame.draw.rect(sc, orange, pygame.Rect(x1 + 2, y1 + 2, 11, 11))
#         for pack in packs:
#             pygame.draw.rect(sc, Color(199, 119, 28), pygame.Rect(220 + pack[0] * 17,
#                                                                   27 + pack[1] * 17 + 1 if pack[1] == 0 else 27 + pack[
#                                                                       1] * 17, 15 * pack[2], 15 * pack[3]))
#
#         # обновляем окно
#         pygame.display.update()
#         clock.tick(fps)
