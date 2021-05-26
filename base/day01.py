# ——————————————————————————
# -*- coding: utf-8 -*-
# @file   : day01.py
# @Time   : 2021/5/25 16:46
# ——————————————————————————

aname = '皖晴'

print(aname)


def fun1():
    a = '2021.5.25'
    print(a)


def fun2(a):
    print(a)


a = 0


def a_fun():
    a = 1
    print(a)
    pass


def a_fun1():
    global a
    a = 2
    print(a)


if __name__ == '__main__':
    # fun1()
    # fun2(aname)
    # aname = 'lyc'
    # fun2(aname)
    #     a_fun()
    #     a_fun1()
    #     print(a)
    a_fun1()
    a = 'abc'
    print(a)
