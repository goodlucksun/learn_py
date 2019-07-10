#! /usr/local/opt/python/libexec/bin python3


#   split   #  将字符串分成列表

sentence = "When I finally decided to get up, It's nine o'clock."

sp_sentence = sentence.split()

sp2_sentence = sentence.split(' ', 2) #只使用前两个空格去拆分 ，所以结果会生成三个元素的列表

sp3_sentence = sentence.split(',')

print("output#21: {0}".format(sp_sentence))

print("output#22: PIECE1:{0}, PIECE2:{1}, PIECE3:{2}".format(sp2_sentence,sp2_sentence[2],sp3_sentence))


# join #  列表组合成字符串

print("output#23: {0}".format(','.join(sp3_sentence)))
str3_kg = '    '
str3 = "I'm sleepy"
str4 = str3_kg.join(str3)
print("output#24: {0}".format(str4))


#strip# 去除首位特殊符号  \n \t

str5= str3_kg+str3+str3_kg

print("output#25: {0:s}".format(str5.strip()))
print("output#26: {0:s}".format(str5.rstrip()))
print("output#27: {0:s}".format(str5.lstrip()))

#replace#

str6 = "This sentence include a lot of blank ."


print("output#28: {0:s}".format(str6.replace(' ','!')))

print("output#28: {0:s}".format(str6.replace('a','!')))


#lower upper capitalize#  capitalize 每个单词的首字母大写

str7 = str6.upper()


print("output#29: {0:s}".format(str7))
print("output#30: {0:s}".format(str7.capitalize()))

str6_list = str6.split()

print("output#31: (change each word):")
for word in str6_list:
    print("{0:s}".format(word.capitalize()))
