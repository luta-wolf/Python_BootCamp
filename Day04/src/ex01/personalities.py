def fix_wiring(cables, sockets, plugs):
    # Фильтруем нестроковые элементы входных итераторов
    cables = filter(lambda x: isinstance(x, str), cables)
    sockets = filter(lambda x: isinstance(x, str), sockets)
    plugs = filter(lambda x: isinstance(x, str), plugs)
    # Создаем список для результирующих строк
    result = []
    # Итерируемся по кабелям и соответствующим им розеткам и штекерам
    for cable, socket, plug in zip(cables, sockets, plugs):
        # Если есть штекер, то используем его
        if plug:
            result.append(f"plug {cable} into {socket} using {plug}")
        # Иначе свариваем кабель и розетку
        else:
            result.append(f"weld {cable} to {socket} without plug")
    # Возвращаем итератор по строкам
    return iter(result)


def main():
    plugs = ['plug1', 'plug2', 'plug3']
    sockets = ['socket1', 'socket2', 'socket3', 'socket4']
    cables = ['cable1', 'cable2', 'cable3', 'cable4']
    fix_wiring(plugs, sockets, cables)
    for c in fix_wiring(cables, sockets, plugs):
        print(c)
    print('-' * 20)
    plugs = ['plugZ', None, 'plugY', 'plugX']
    sockets = [1, 'socket1', 'socket2', 'socket3', 'socket4']
    cables = ['cable2', 'cable1', False]

    for c in fix_wiring(cables, sockets, plugs):
        print(c)


if __name__ == "__main__":
    main()
