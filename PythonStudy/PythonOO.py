#python���������

class student(object):
    def __init__(self, name, score):
        self.name=name
        self.score=score

    def print_self(self):
        print '%s:%s' %(self.name,self.score)

student('zhangsan',59).print_self()

#ǰ׺����__�ͱ����private 

#���Ƶ�get set����


#�̳�
class Animal(object):
    def run(self):
        print 'Annimal is running'

class Dog(Animal):
    pass

class Cat(Animal):
    pass

Dog().run()

##��̬

##����չ����
##���޸ķ��


#ʹ��type()�ж϶�������
print type(123)
print type('123')
print type(abs)

import types

print type('abc')==types.StringType
print type([])==types.ListType
print type(())==types.TupleType

#ʹ��isinstance()



#ʹ��dir() ��ȡһ��������������Ժͷ���
print dir([])

print 'ABC'.lower()

#���Զ����Ƿ�������
print hasattr('ABC','x')