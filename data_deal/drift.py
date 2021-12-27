# -*- coding: utf-8 -*-
# @Time    : 2021/9/22 16:01
# @Author  : Zy
# @File    : drift.py
# @Software: PyCharm
import re

a = '01:05:00'
c = "%d" % (1)
d = c.zfill(2)
print(d)
b = re.compile(d + ':[0-9]{2}:[0-9]{2}')

print(re.match(b, a))
