# ——————————————————————————
# -*- coding: utf-8 -*-
# @file   : mode_demo2.py
# @Time   : 2021/5/28 16:58
# ——————————————————————————

# from base.mode_demo import a_fun
# import mode_demo
from base import mode_demo

# a_fun()
mode_demo.a_fun()
print(mode_demo.a)

import json

adict = {'name': '孙皖晴',
         '爱称': '宝贝',
         '别称': ["小孙", "皖晴"],
         'age': 26}
print(type(adict))

# 字典转字符串
astr = json.dumps(adict, ensure_ascii=False)
print(astr)
print(type(astr))

# 字符串转字典
bstr = '{"name": "孙皖晴",\
         "爱称": "宝贝",\
         "别称": ["小孙", "皖晴"],\
         "age": 26}'
print(bstr)
print(type(bstr))
bdict = json.loads(bstr)
print(bdict)
print(type(bdict))
