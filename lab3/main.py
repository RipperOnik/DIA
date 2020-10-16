from lab_python_fp.field import field
from lab_python_fp.gen_random import gen_random
from lab_python_fp.unique import Unique
from lab_python_fp.sort import sort
from lab_python_fp.print_result import print_result
from lab_python_fp.cm_timer import *
import time
from lab_python_fp.process_data import *
import json

@print_result
def test_1():
    return 1


@print_result
def test_2():
    return 'iu5'


@print_result
def test_3():
    return {'a': 1, 'b': 2}


@print_result
def test_4():
    return [1, 2]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    goods = [
        {'title': 'Ковер', 'price': 2000, 'color': 'green'},
        {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
    ]
    print("Example Gen ")
    print(list(field(goods, 'title')))
    print(list(field(goods, 'title', 'price')))
    count = 5
    print("Example Gen_Random")
    for i in gen_random(count, 1, 3):
        print(i)
    print("Example Unique iterator")
    data = [1, 1, 1, 1, 2, 2, 2, 2]
    data1 = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
    for i in Unique(data, ignore_case=True):
        print(i)
    for i in Unique(data1, ignore_case=True):
        print(i)
    data = gen_random(4, 1, 10)
    for i in Unique(data, ignore_case=True):
        print(i)
    print("Example sort")
    data2 = [4, -30, 100, -100, 123, 1, 0, -1, -4]
    res = sort(data2)
    print(res)
    res_lambda = (lambda arr: sort(arr))(data2)
    print(res_lambda)

    print("Example decorator")
    test_1()
    test_2()
    test_3()
    test_4()

    print("Example timer")
    with cm_timer1():
        time.sleep(0.1)
    with cm_timer2():
        time.sleep(0.1)

    path = "./package.json"

    # Необходимо в переменную path сохранить путь к файлу, который был передан при запуске сценария

    with open(path) as f:
        data = json.load(f)  # список словарей

    with cm_timer1():
        print(f4(f3(f2(f1(data)))))


    







