import pygame
from pygame import Color

fps = 150

win_width = 1600
win_height = 800

white = (255, 255, 255)
orange = (255, 150, 100)
black = (0, 0, 0)
clock = pygame.time.Clock()
pygame.init()
font_style = pygame.font.Font('my_font.ttf', 24)


def message(sc, msg, color, x, y):
    msg = str(msg)
    mesg = font_style.render(msg, True, color)
    sc.blit(mesg, (x, y))


def get_from_db(packs, new_pack=None):
    sc = pygame.display.set_mode((win_width, win_height))
    flag = True
    flag2 = True
    y_now = 0
    x_now = 0
    while 1:
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                pygame.display.quit()
                return
        # заливаем фон
        sc.fill(white)
        # рисуем легенду
        print_legend(sc)
        # рисуем склад
        print_warehouse(sc)

        for pack in packs:
            y = pack[1]
            y = (y // 10) * 10 + y
            x1 = 220 + pack[0] * 15 + pack[0] * 2
            y1 = 27 + y * 15 + y * 2
            height = 15 * pack[2] + (pack[2] - 1) * 2
            width = 15 * pack[3] + (pack[3] - 1) * 2
            print_box(sc, x1, y1, width, height)

        if new_pack is not None:
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
            print_box(sc, x_now, y_now, width, height)

        # обновляем окно
        pygame.display.update()
        clock.tick(fps)


def animation_added_package(prevent_packages, new_package, another_packs):
    sc = pygame.display.set_mode((win_width, win_height))
    ind = [0 for _ in range(len(prevent_packages))]
    y_con = [0 for _ in range(len(prevent_packages))]
    jkh = 170
    jkh_i = 1
    flag = False
    flag2 = True
    flag3 = True
    flag4 = False
    new_x_now = 0
    new_y_now = 0
    while 1:
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                pygame.display.quit()
                return
        # заливаем фон
        sc.fill(white)
        # рисуем легенду
        print_legend(sc)
        # рисуем склад
        print_warehouse(sc)

        for pack in another_packs:
            y = pack[1]
            y = (y // 10) * 10 + y
            x1 = 220 + pack[0] * 15 + pack[0] * 2
            y1 = 27 + y * 15 + y * 2
            height = 15 * pack[2] + (pack[2] - 1) * 2
            width = 15 * pack[3] + (pack[3] - 1) * 2
            print_box(sc, x1, y1, width, height)
        if not flag4:
            for pack in prevent_packages:
                y = pack[1]
                y = (y // 10) * 10 + y
                height = 15 * pack[2] + (pack[2] - 1) * 2
                width = 15 * pack[3] + (pack[3] - 1) * 2
                x_now = 220 + pack[0] * 15 + pack[0] * 2
                y_now = 27 + y * 15 + y * 2 + ind[prevent_packages.index(pack)]
                y_con[prevent_packages.index(pack)] = 27 + y * 15 + y * 2 + jkh
                if y_now != y_con[prevent_packages.index(pack)]:
                    ind[prevent_packages.index(pack)] += jkh_i
                else:
                    flag = True
                    if not jkh:
                        flag4 = True
                        for b in prevent_packages:
                            another_packs.append(b)
                print_box(sc, x_now, y_now, width, height)

        if (flag or not prevent_packages) and new_package:
            y = new_package[1]
            y = (y // 10) * 10 + y
            height = 15 * new_package[2] + (new_package[2] - 1) * 2
            width = 15 * new_package[3] + (new_package[3] - 1) * 2
            x_res = 220 + new_package[0] * 15 + new_package[0] * 2
            y_res = 27 + y * 15 + y * 2
            if flag2:
                new_x_now = 218 - width
                new_y_now = 790 - height
                flag2 = False
            new_y_con = 197 if y < 11 else 537
            if new_y_now != new_y_con and flag3:
                new_y_now -= 1
            else:
                flag3 = False
                if new_x_now != x_res:
                    new_x_now += 1
                else:
                    if new_y_now != y_res:
                        new_y_now -= 1
                    else:
                        jkh = 0
                        jkh_i = -1
            print_box(sc, new_x_now, new_y_now, width, height)
        # обновляем окно
        pygame.display.update()
        clock.tick(fps)


def animation_unload_package(prevent_packages, unload_package, another_packs, update_packs=None):
    sc = pygame.display.set_mode((win_width, win_height))
    flag = False
    flag2 = True
    flag3 = True
    flag4 = False
    unload_package_x_now = 0
    unload_package_y_now = 0
    ind = [0 for _ in range(len(prevent_packages))]
    # ind1 = [0 for _ in range(len(update_packs))]
    y_con = [0 for _ in range(len(prevent_packages))]
    # y_con1 = [0 for _ in range(len(update_packs))]
    jkh = 170
    jkh_i = 1
    while 1:
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                pygame.display.quit()
                return
        # заливаем фон
        sc.fill(white)
        # рисуем легенду
        print_legend(sc)
        # рисуем склад
        print_warehouse(sc)

        for pack in another_packs:
            y = pack[1]
            y = (y // 10) * 10 + y
            x1 = 220 + pack[0] * 15 + pack[0] * 2
            y1 = 27 + y * 15 + y * 2
            height = 15 * pack[2] + (pack[2] - 1) * 2
            width = 15 * pack[3] + (pack[3] - 1) * 2
            print_box(sc, x1, y1, width, height)
        if not flag4:
            for pack in prevent_packages:
                y = pack[1]
                y = (y // 10) * 10 + y
                height = 15 * pack[2] + (pack[2] - 1) * 2
                width = 15 * pack[3] + (pack[3] - 1) * 2
                x_now = 220 + pack[0] * 15 + pack[0] * 2
                y_now = 27 + y * 15 + y * 2 + ind[prevent_packages.index(pack)]
                y_con[prevent_packages.index(pack)] = 27 + y * 15 + y * 2 + jkh
                if y_now != y_con[prevent_packages.index(pack)]:
                    ind[prevent_packages.index(pack)] += jkh_i
                else:
                    flag = True
                    if not jkh:
                        flag4 = True
                        for b in prevent_packages:
                            another_packs.append(b)
                print_box(sc, x_now, y_now, width, height)

        if flag and unload_package:
            y = unload_package[1]
            y = (y // 10) * 10 + y
            height = 15 * unload_package[2] + (unload_package[2] - 1) * 2
            width = 15 * unload_package[3] + (unload_package[3] - 1) * 2
            if flag2:
                unload_package_x_now = 220 + unload_package[0] * 15 + unload_package[0] * 2
                unload_package_y_now = 27 + y * 15 + y * 2
                flag2 = False
            unload_package_con = 27 + y * 15 + y * 2 + 170
            if unload_package_y_now != unload_package_con and flag3:
                unload_package_y_now += 1
            else:
                flag3 = False
                if unload_package_x_now != 1325:
                    unload_package_x_now += 1
                else:
                    if unload_package_y_now != 790 - height:
                        unload_package_y_now += 1
                    else:
                        jkh = 0
                        jkh_i = -1
                        unload_package = None
            print_box(sc, unload_package_x_now, unload_package_y_now, width, height)
        else:
            if unload_package:
                y = unload_package[1]
                y = (y // 10) * 10 + y
                height = 15 * unload_package[2] + (unload_package[2] - 1) * 2
                width = 15 * unload_package[3] + (unload_package[3] - 1) * 2
                x = 220 + unload_package[0] * 15 + unload_package[0] * 2
                y = 27 + y * 15 + y * 2
                print_box(sc, x, y, width, height)

        # обновляем окно
        pygame.display.update()
        clock.tick(fps)


def print_legend(sc):
    pygame.draw.rect(sc, black, pygame.Rect(370, 720, 15, 15), 2)
    pygame.draw.rect(sc, orange, pygame.Rect(372, 722, 11, 11))
    message(sc, "Лента загрузки/выгрузки", black, 390, 710)

    pygame.draw.rect(sc, Color(34, 82, 17), pygame.Rect(370, 760, 15, 15), 2)
    pygame.draw.rect(sc, Color(62, 173, 23), pygame.Rect(372, 762, 11, 11))
    message(sc, "Лента хранения", black, 390, 750)

    pygame.draw.rect(sc, Color(34, 82, 17), pygame.Rect(730, 720, 15, 15), 2)
    pygame.draw.rect(sc, Color(176, 189, 172), pygame.Rect(732, 722, 11, 11))
    message(sc, "Лента транспортировки", black, 750, 710)

    pygame.draw.rect(sc, Color(34, 82, 17), pygame.Rect(730, 760, 15, 15), 2)
    pygame.draw.rect(sc, Color(199, 119, 28), pygame.Rect(732, 762, 11, 11))
    message(sc, "Коробка", black, 750, 750)

    pygame.draw.rect(sc, Color(34, 82, 17), pygame.Rect(930, 760, 15, 15), 2)
    pygame.draw.rect(sc, Color("red"), pygame.Rect(932, 762, 11, 11))
    message(sc, "Сканер", black, 950, 750)


def print_warehouse(sc):
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
    pygame.draw.rect(sc, Color("red"), pygame.Rect(215, 730, 20, 30))


def print_box(sc, x1, y1, width, height):
    pygame.draw.rect(sc, Color(199, 119, 28), pygame.Rect(x1, y1, width, height))
