#! /usr/local/opt/python/libexec/bin python3

from math import exp, log, sqrt

import re

#datatime模块 python
from datetime import date, time, datetime, timedelta
#{0!s}代表格式化转换为字符串型输出
today = date.today()
print("output #41: today:{0!s}".format(today))
print("output #42: today:{0!s}".format(today.year))
print("output #43: today:{0:d}".format(today.year))
print("output #44: today:{0!s}".format(datetime.today()))

#
one_day = timedelta(days=-1)
yesterday = today + one_day
print("output #45: today:{0!s}".format(yesterday))
