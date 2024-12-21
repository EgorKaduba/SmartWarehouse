from WarehouseSystem import WarehouseSystem

warehouse = WarehouseSystem()
warehouse.read_db()
while True:
    choice = int(
        input("Выберите действие: \n1 - Вывести склад\n2 - Добавить новый товар\n3 - Выгрузить товар\n4 - Выход\n"))
    if choice == 1:
        warehouse.print_cells()
    elif choice == 2:
        warehouse.add_package(input("Введите информацию о новом товаре: "))
    elif choice == 3:
        warehouse.unloading_package([int(i) for i in input("Введите список id товаров: ").split(' ')])
    else:
        break
