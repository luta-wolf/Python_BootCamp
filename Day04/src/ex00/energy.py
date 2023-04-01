from itertools import zip_longest

def fix_wiring(cables, sockets, plugs):
    # Фильтруем нестроковые элементы входных итераторов
    cables = filter(lambda x: isinstance(x, str) and x.startswith('cable'), cables)
    sockets = filter(lambda x: isinstance(x, str) and x.startswith('socket'), sockets)
    plugs = filter(lambda x: isinstance(x, str) and x.startswith('plug'), plugs)
    # Создаем список для результирующих строк
    result = []
    # Создаем кортежи со всеми вариантами
    all_var = (zip_longest(*list(zip(*zip(cables, sockets))), plugs))
    # Итерируемся по кабелям и соответствующим им розеткам и штекерам
    for cable, socket, plug in all_var:
        # Если есть штекер, то используем его
        if plug and socket:
            result.append(f"plug {cable} into {socket} using {plug}")
        # Иначе свариваем кабель и розетку
        elif socket:
            result.append(f"weld {cable} to {socket} without plug")
    # Возвращаем итератор по строкам
    return iter(result)


def main():
    plugs = ['plug1', 'plug2', 'plug3']
    sockets = ['socket1', 'socket2', 'socket3', 'socket4']
    cables = ['cable1', 'cable2', 'cable3', 'cable4']
    fix_wiring(cables, sockets, plugs)
    for c in fix_wiring(cables, sockets, plugs):
        print(c)
    print('-' * 20)
    plugs = ['plugZ', None, 'plugY', 'plugX']
    sockets = [1, 'socket1', 'socket2', 'socket3', 'socket4']
    cables = ['cable2', 'cable1', False, 'sss']

    for c in fix_wiring(cables, sockets, plugs):
        print(c)


if __name__ == "__main__":
    main()
