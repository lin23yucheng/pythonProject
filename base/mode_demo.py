# ——————————————————————————
# -*- coding: utf-8 -*-
# @file   : mode_demo.py
# @Time   : 2021/5/28 16:48
# ——————————————————————————

a = '变量a'


def a_fun():
    a = 'a_fun的变量a'
    print(a)
    pass


def a_fun1():
    global a
    a = 'lalalalala'


if __name__ == '__main__':
    print(a)
    a_fun()
    a_fun1()
    print(a)
    a = 520
    print(a)

