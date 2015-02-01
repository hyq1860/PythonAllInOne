#python的面向对象

class student(object):
    def __init__(self, name, score):
        self.name=name
        self.score=score

    def print_self(self):
        print '%s:%s' %(self.name,self.score)

student('zhangsan',59).print_self()

#前缀加上__就变成了private 

#类似的get set方法


#继承
class Animal(object):
    def run(self):
        print 'Annimal is running'

class Dog(Animal):
    pass

class Cat(Animal):
    pass

Dog().run()

##多态

##对扩展开放
##对修改封闭


#使用type()判断对象类型
print type(123)
print type('123')
print type(abs)

import types

print type('abc')==types.StringType
print type([])==types.ListType
print type(())==types.TupleType

#使用isinstance()



#使用dir() 获取一个对象的所有属性和方法
print dir([])

print 'ABC'.lower()

#测试对象是否有属性
print hasattr('ABC','x')