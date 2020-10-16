from lab_python_fp.print_result import *
from lab_python_fp.sort import sort
from lab_python_fp.field import field
from lab_python_fp.unique import Unique
from lab_python_fp.gen_random import gen_random


#@print_result
def f1(data):
    return sort(Unique(field(data, "job-name"), ignore_case=True)) # удаление дубликатов и сортировка по алфавиту


@print_result
def f2(f1arr):
    return list(filter(lambda x: x[:11].upper() == "программист".upper(), f1arr))


@print_result
def f3(f2arr):
    return list(map(lambda x: x + " с опытом Python", f2arr))


@print_result
def f4(f3arr):
    pairs = list(zip(f3arr, [" с зарплатой {} рублей".format(zp) for zp in gen_random(len(f3arr), 100000, 200000)]))
    return ["{}{}".format(pair[0], pair[1]) for pair in pairs]

