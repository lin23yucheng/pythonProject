# ——————————————————————————
# -*- coding: utf-8 -*-
# @file   : day02.py
# @Time   : 2021/5/28 13:37
# ——————————————————————————

def bool_demo():
    a = True
    b = False
    print(a, b)
    print(type(a))
    print(type(b))


def none_demo():
    a = None
    print(a)
    print(type(a))


def list_demo():
    alist = ['swq', 'lyc', '十一十七', 3.1415926, '英雄联盟', 849236000]
    print(alist[-1])
    print(alist[0:3])
    # 跳过一个取
    print(alist[::2])
    print(alist[::3])
    # 倒着打印
    print(alist[::-1])


def list_delete():
    blist = ['swq', 'lyc', '十一十七', 3.1415926, '英雄联盟', 849236000]
    blist.pop(3)
    # 不写默认删除最后一个
    b = blist.pop()
    # 指定元素删除
    blist.remove('英雄联盟')
    print(blist)
    print(b)


def list_add():
    clist = ['swq', 'lyc', '十一十七', 3.1415926, '英雄联盟', 849236000]
    clist.append('融创乐园')
    print(clist)
    dlist = ['000', 123]
    clist.extend(dlist)
    print(clist)
    clist.append(dlist)
    print(clist)


def list_demo3():
    alist = ['swq', 'lyc', '十一十七', 3.1415926, '英雄联盟', 849236000]
    alist[2] = 666
    print(alist)


def list_demo4():
    # 数字排序从小到大
    alist = [51, 88, 45, 3.1415926, 6, 78]
    alist.sort()
    print(alist)
    # 数字排序从大到小
    alist.sort(reverse=True)
    print(alist)


def list_demo5():
    # 去重
    alist = [51, 88, 45, 3.1415926, 88, 88]
    s = set(alist)
    print(s)
    print(type(s))
    blist = list(s)
    print(blist)


def tuple_demo():
    # 元祖
    atuple = (555, 665, '双方的', '速度速度')
    print(atuple[0])
    print(atuple[-1])
    print(atuple[1:3])
    # 元祖类型不能增加 修改 删除 更新
    btuple = (855, 'lyc')
    c = atuple + btuple
    print(c)


def dict_demo():
    # 字典
    adict = {'name': '孙皖晴', '爱称': '宝贝', '别称': ["小孙", "皖晴"], 'age': 26}
    print(adict)
    print(adict['别称'])
    adict['age'] = 25
    print(adict)
    adict.pop('name')
    print(adict)
    adict['job'] = '律师'
    print(adict)
    # 合并字典,改变了原始字典数据
    bdict = {'a': 1, 'b': 2}
    adict.update(bdict)
    print(adict)
    # 合并字典,不改变原始字典数据
    cdict = {'lin': '林', 'yu': '禹'}
    ddict = {'sun': '孙', 'wan': '皖'}
    edict = dict(cdict, **ddict)
    print(cdict)
    print(ddict)
    print(edict)


if __name__ == '__main__':
    # bool_demo()
    # none_demo()
    # list_delete()
    # list_add()
    # list_demo3()
    # list_demo4()
    # list_demo5()
    # tuple_demo()
    dict_demo()
