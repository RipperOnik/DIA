# используется для сортировки
from operator import itemgetter


class Computer:
    def __init__(self, id, model, os_id, performance):
        self.id = id
        self.model = model
        self.os_id = os_id
        self.performance = performance


class Os:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class ComputerOs:
    def __init__(self, os_id, com_id):
        self.os_id = os_id
        self.com_id = com_id


# Компьютеры
comps = [Computer(1, "IBM-1", 1, 100), Computer(2, "Lenovo Gaming PC", 4, 400), Computer(3, "IBM-2", 2, 110),
         Computer(4, "Intel PC", 3, 200), Computer(5, "Asus Gaming PC", 4, 500)]


# Операционные системы
op_systems = [Os(1, "Linux"), Os(2, "Windows 7"), Os(3, "Windows 8"), Os(4, "Windows 10")]


# Компьютеры операционных систем
comp_os = [ComputerOs(1, 1), ComputerOs(2, 3), ComputerOs(3, 4), ComputerOs(4, 2), ComputerOs(4, 5),
           ComputerOs(4, 1), ComputerOs(3, 1)]


def main():
    one_to_many = [(c.model, c.performance, o.name) for o in op_systems for c in comps if c.os_id == o.id]

    many_to_many_temp = [(o.name, cs.os_id, cs.com_id) for o in op_systems for cs in comp_os if o.id == cs.os_id]

    many_to_many = [(c.model, os_name)
                    for os_name, os_id, com_id in many_to_many_temp
                    for c in comps if c.id == com_id]
    print(one_to_many)
    print(many_to_many)
    print("Задание 1")
    temp = [(pc[2], pc[0]) for pc in one_to_many if pc[2][0] == "W"]
    temp_os = [pc[0] for pc in temp]
    temp_os = set(temp_os)
    res1 = {}
    for os in temp_os:
        list_pc = [pc[1] for pc in temp if os == pc[0]]
        res1[os] = list_pc
    print(res1)

    print("Задание 2")
    list_os = [pc[2] for pc in one_to_many]
    list_os = set(list_os)
    list_os_perf_best = []
    for os in list_os:
        list_os_perf = [(os, pc[1]) for pc in one_to_many if os == pc[2]]
        list_os_perf_temp = sorted(list_os_perf, key=itemgetter(1), reverse=True)
        list_os_perf_best.append(list_os_perf_temp[0])
    res2 = sorted(list_os_perf_best, key=itemgetter(1), reverse=True)
    print(res2)

    print("Задание 3")
    res3 = sorted(many_to_many, key=itemgetter(1))
    print(res3)


if __name__ == '__main__':
    main()

