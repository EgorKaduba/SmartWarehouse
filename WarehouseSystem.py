from math import ceil
from Package import Package
import pg


class WarehouseSystem:
    def __init__(self):
        self.cells = [[0 for _ in range(65)] for __ in range(20)]

    def read_db(self):
        res = []
        with open("data.txt", "r", encoding='utf-8') as file:
            lines = file.readlines()
            for line in lines:
                line = line.replace('\n', '')
                if line.split(';')[-1] == "Хранится на складе":
                    i_min = int(line.split(';')[8].split(':')[0].split('x')[0]) - 1
                    i_max = int(line.split(';')[8].split(':')[1].split('x')[0])
                    j_min = int(line.split(';')[8].split(':')[0].split('x')[1]) - 1
                    j_max = int(line.split(';')[8].split(':')[1].split('x')[1])
                    for i in range(i_min, i_max, 1):
                        for j in range(j_min, j_max, 1):
                            self.cells[i][j] = int(line.split(';')[0])
                    res.append([j_min, i_min, i_max - i_min, j_max - j_min])
        return res

    def print_cells(self):
        for i in range(len(self.cells)):
            if i % 10 == 0:
                print("--------------------")
            print(self.cells[i])
        pg.get_from_db(self.read_db())

    def add_package(self, info: str):
        new_pack = Package()
        new_pack.reading_QR(info)
        pos = self.add_cell_in_cells(new_pack.size[0], new_pack.size[1], new_pack.id)
        if not pos:
            return False
        new_pack.position = pos
        try:
            with open("data.txt", mode='a', encoding='utf-8') as file:
                file.write("\n" + str(new_pack))
        except FileNotFoundError as error_msg:
            print(error_msg)
            return False
        pg.get_from_db(self.read_db()[:-1],  new_pack=self.read_db()[-1])
        return True # Москва ул. Утренняя;Пушкино ул. Набережная;22.12.2024;15x15x15;15.5;AAA

    @staticmethod
    def get_all_packages() -> list:
        try:
            with open("data.txt", mode='r', encoding='utf-8') as file:
                return [line.replace('\n', '') for line in file.readlines()]
        except FileNotFoundError as error_msg:
            print(error_msg)
            return []

    def add_cell_in_cells(self, size_x, size_y, package_id):
        size_x = ceil(size_x / 15)
        size_y = ceil(size_y / 15)
        for line in range((len(self.cells) // 10) - 1, -1, -1):
            for i in range(10):
                pos_i = i + line * 10
                for pos_j in range(64, -1, -1):
                    i_max = size_x + pos_i
                    j_min = pos_j - size_y
                    if i_max - line * 10 <= 10:
                        if self.check(pos_i, i_max, j_min, pos_j):
                            for k in range(pos_i, i_max):
                                for h in range(pos_j, j_min, -1):
                                    self.cells[k][h] = package_id
                            return [pos_i + 1, j_min + 2, i_max, pos_j + 1] #1 65 3 65
        return []

    def check(self, i_min, i_max, j_min, j_max):
        for i in range(i_min, i_max):
            for j in range(j_max, j_min, -1):
                if self.cells[i][j] != 0:
                    return False
        return True

    def remove_cell_from_cells(self, package_id):
        for i in range(len(self.cells)):
            for j in range(len(self.cells[i])):
                if self.cells[i][j] == package_id:
                    self.cells[i][j] = 0

    def unloading_package(self, packs_id):
        all_package = self.get_all_packages()
        for i in range(len(all_package)):
            for id_pack in packs_id:
                if int(all_package[i].split(';')[0]) == id_pack and all_package[i].split(';')[-1] == 'Хранится на складе':
                    self.remove_cell_from_cells(id_pack)
                    all_package[i] = all_package[i].replace('Хранится на складе', 'Выгружен')
        with open('data.txt', mode='w', encoding='utf-8') as file:
            file.writelines(f"{item}\n" for item in all_package[:-1])
            file.writelines(all_package[-1])

    def update_cells(self):
        for i in self.cells:
            for j in self.cells:
                pass
