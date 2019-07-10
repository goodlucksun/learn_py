#!/usr/local/opt/python/libexec/bin python3

from math import exp, log, sqrt
import re

#首先介绍的有re.compile re.search re.sub re.ignorecase re.I
#正则表达式不是必须编译的，但是编译可以提高运算速度，


#search 查找
str = "The lovely cat has no opportunity to get his next generation."
str_list = str.split()
pattern = re.compile(r"e",re.I)   #r""为不处理转义字符   re.I 为不区分大小写
count = 0
for i in str_list:
    if pattern.search(i):
        count += 1
print("output#38: {0:d}".format(count))

#match 匹配
print("ouput#39: ")
pattern2 = re.compile(r"(?P<match_word>e)",re.I)
for word in str_list:
    if pattern2.search(word):
        print("{:s}".format(pattern2.search(word).group('match_word')))

#sub 替换
str_to_find_e = r"e"
pattern3 = re.compile(str_to_find_e)
print("output#40: {:s}".format(pattern.sub("E",str)))
