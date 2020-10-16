def field(items, *args): # генератор, возвращающий поля с заданным ключом и словари
    assert len(items) > 0 and isinstance(items, list)
    if len(args) == 1:
        for i in range(len(items)):
            for key, value in items[i].items():
                if key == args[0]:  # если передан один аргумент, возвращаем поля с ним
                    yield value

    else:
        for i in range(len(items)):
            dictionary = {}
            for key, value in items[i].items():
                for arg in args:    # если передано много аргументов, то возвращаем словари сзаданными ключами
                    if key == arg:
                        dictionary[key] = items[i][key]
                        break   # как только нужный аргумент подошел к ключу, выходим из цикла (оптимизация)
            yield dictionary





