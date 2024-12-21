from datetime import datetime as dt


class Package:
    def __init__(self):
        self.id = 0
        self.place_of_departure = ""
        self.destination = ""
        self.arrival_date = dt.today().strftime("%d.%m.%Y")
        self.unloading_time = ""
        self.size = list()
        self.weight = 0
        self.product_name = ""
        self.position = list()
        self.status = ""

    def __str__(self):
        size = f"{self.size[0]}x{self.size[1]}x{self.size[2]}"
        pos = f"{self.position[0]}x{self.position[1]}:{self.position[2]}x{self.position[3]}"
        if all([self.id, self.place_of_departure, self.destination, self.arrival_date, self.unloading_time, size,
                self.weight, self.product_name, self.status, pos]):
            return (f"{self.id};{self.place_of_departure};{self.destination};{self.arrival_date};{self.unloading_time};"
                    f"{size};{self.weight};{self.product_name};{pos};{self.status}")

    def reading_QR(self, my_string: str):
        try:
            parametrs_list = list(my_string.split(";"))
            parametrs_list[3] = list(int(x) for x in parametrs_list[3].split('x'))
            parametrs_list[4] = float(parametrs_list[4])
            parametrs_keys = ['Пункт отправления', 'Пункт назначения', 'Дата отправления', 'Размеры', 'Вес',
                              'Наименование']
            parametrs_dict = dict(zip(parametrs_keys, parametrs_list))
            if self.check_QR(parametrs_dict):
                with open("data.txt", mode="r") as file:
                    data = file.read()
                    if not data:
                        self.id = 1
                    else:
                        self.id = int(data.split('\n')[-1].split(';')[0]) + 1
                self.place_of_departure = parametrs_dict['Пункт отправления']
                self.destination = parametrs_dict['Пункт назначения']
                self.unloading_time = parametrs_dict['Дата отправления']
                self.size = parametrs_dict['Размеры']
                self.weight = parametrs_dict['Вес']
                self.product_name = parametrs_dict['Наименование']
                self.status = "Хранится на складе"
        except Exception as error_msg:
            print(error_msg)

    @staticmethod
    def check_QR(parametrs: dict) -> bool:
        if all(parametrs.values()):
            try:
                date = dt.strptime(parametrs['Дата отправления'], '%d.%m.%Y')
                dt_today = dt.strptime(dt.today().strftime('%d.%m.%Y'), '%d.%m.%Y')
                if dt_today > date:
                    return False
            except ValueError as error_msg:
                print(error_msg)
                return False
            if not ((15 <= parametrs['Размеры'][0] <= 500) and (15 <= parametrs['Размеры'][1] <= 150) and (
                    0 < parametrs['Размеры'][2] < 500)):
                return False
            if not (0 < parametrs['Вес'] < 100):
                return False
            return True
        return False
