#! /usr/local/opt/python/libexec/bin python3

print("output#1: I'm excited to learn python3")

x=4
y=5
z=x+y
print("output#2: four plus five equal {0:d}".format(z))
###使用.format 代替  print(“z”) 可以更加规范


a = [1,2,3,4]
b = ['first','second','third','forth']
c = a + b
print("output#3: {0},{1},{2}".format(a,b,c))



print("output#7: {0:.1f}".format(10/3))


print("output#8: {0:.3f}".format(10**2))
