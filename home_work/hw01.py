# ——————————————————————————
# -*- coding: utf-8 -*-
# @file   : hw01.py
# @Time   : 2021/5/25 17:28
# ——————————————————————————

a = 10
b = 20


def fun1(n1, n2):
    print(n1 + n2)
    print(type(n1))


def fun2(n1, n2):
    print(n1 - n2)
    print(type(n1))


# 整数转小数
def int2float():
    aint = 100
    print(type(aint))
    afloat = float(aint)
    print(afloat)
    print(type(afloat))


# 小数转整数
def float2int():
    bfloat = 20.52
    print(type(bfloat))
    bint = int(bfloat)
    print(bint)
    print(type(bint))


# 四舍五入
def round_demo():
    cfloat = 8.655
    print('8.655 四舍五入 不保留小数 =', round(cfloat))
    dfloat = 1.356
    print('1.356 四舍五入 保留2小数 =', round(dfloat, 2))
    efloat = 1.8887
    print('1.8887 四舍五入 保留3小数 =', round(efloat, 3))


def str_demo():
    gf = '皖晴小宝贝'
    zy = "执业律师"
    # 三个单引号 通常用于 多行字符
    xj = '''
    淮南
    师范
    学院
    '''

    print(gf[-3:])
    print(gf[:2])
    print(gf[2:5])
    myjj = "孔子曰:\"学而时习之不亦说乎\""
    mujj2 = '孔子曰:"己所不欲勿施于人"'
    myjj3 = '孔子曰:\n"三人行\n必有我师焉\"'
    print(myjj)
    print(mujj2)
    print(myjj3)
    print('123456\t', end='+')
    print('\tqwer')
    # \\ ：代表\本身
    print('1\\2')
    # \ ：（在行尾时）：续行符
    print('123 \
          456')


def str_join():
    age = 27
    name = '小明'
    job = '软件测试工程师'
    print(name + ',' + str(age) + '岁,' + '是一名' + job)

    # %s :占位符
    print('我叫%s,今年%s岁,是一名%s' % (name, age, job))

    # format :格式化
    print('我叫{},今年{}岁,是一名高级{}'.format(name, age, job))

    # f :格式化
    print(f'我叫{name},今年{age}岁,是一名超高级{job}')


def str_fun():
    astr = 'lyc,19941219,! '
    print(len(astr))

    print(astr.count('9'))

    print(astr.find('0'))
    print(astr.find('1'))

    # 字符串分割
    print(astr.split(','))

    # 首字母转大写
    print(astr.capitalize())

    # 转大写
    print(astr.upper())

    # 转小写
    print(astr.lower())

    # 去掉前后空格
    print(astr.strip())

    # 字符串替换
    a_replace = astr.replace('!', ',.')
    print(a_replace)

    # 替换2个
    b_replace = astr.replace('9', '$', 2)
    print(b_replace)

    b_replace = astr.replace('1', '&', 1)
    print(b_replace)


if __name__ == '__main__':
    # fun1(a, b)
    # fun2(80.88, 100)
    # int2float()
    # float2int()
    # round_demo()
    # str_demo()
    # str_join()
    str_fun()
