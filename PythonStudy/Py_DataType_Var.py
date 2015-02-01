print 'i am 刘德华'
print "i'am 张学友"
print 'i\'am \"黎明'
print 'i \'am \n刘德华'
print 'i \'am \\ 刘德华'

print '''line1
line2
lin3...'''

print True and True
print True and False
print False and False

print True or False
print False or False

print not True
print not False

age=19
if age>=18:
    print '成年'
else:
    print '未成年'


#变量
var_1=1
var_2='1'
Flag=True

a='abc'
b=a
a='xyz'
print b

#常量
PI=3.1415926

print 10/3
print 10.0/3
print 10%3

#Pythond字符串
#Python提供了ord()和chr()函数，可以把字母和对应的数字相互转换
print ord('A')
print chr(65)

#Python添加了Unicode的支持 Unicode表示的字符串用u'zifuchuan'表示
print u'中文'.encode('utf-8')
print '中文'
print 'abc'.decode('utf-8')
print u'中文'.encode('utf-8')

#字符串的长度
print len('ab')
print len(u'中文')

#格式化
print 'Hello,%s' % 'world'

print 'Hello,%s,你有美金%d' % ('张三',10000000)

#list
datalist=['张三','李四']
print datalist
print len(datalist)
print datalist[0]
print datalist[1]

print datalist[len(datalist)-1]
print datalist[-1]
print datalist[-2]

datalist.append('王五')
print datalist[-1]

#删除末尾的元素
datalist.pop()
print datalist
#删除指定位置的元素
datalist.pop(0)
print datalist
#替换某个位置的元素
datalist[0]='liudehua'
print datalist

#list中数据类型可以不同
datalist=['liudehua',1,True,['data',True]]
print datalist

datalist=[]
print datalist
print len(datalist)

#tuple 元组
datatuple=('1','2')
print datatuple;
print datatuple[0]

datatuple=(1)#这是个数字
print datatuple
datatuple=(1,)#这是个数组
print datatuple

#tuple不能变是指他的每个元素的指向不能变 但是里面的内容可变
datatuple=('a','b',['c','d'])
datatuple[2][0]='wo change'
datatuple[2][1]='wo bian'
print datatuple


#条件判断
condition=True
condition=0
if condition:
    print condition
else:
    print '0 as False'


condition=1
if condition:
    print '1 as True'
else:
    print 'false'


condition=[]
if condition:
    print condition
else:
    print 'false'


condition.append(1)
if condition:
    print condition
else:
    print 'false'

condition=''
if condition:
    print condition
else:
    print 'false'

condition='123456'
if condition:
    print condition
else:
    print 'false'


#循环
datalist=['1','2','3']
for item in datalist:
    print item

sum=0
for x in [1,2,3,4,5,6,7,8,9,10]:
    sum = sum + x
print sum;

for x in range(100):
    sum=sum+x
print sum


while sum<5012:
    sum=sum+2
print sum;
    

#raw_input
birth=raw_input('请输入你的年龄：')
if(birth>1990):
    print '90后'
else:
    print '80后'
birth=int(raw_input('请输入你的年龄：'))
if(birth>1990):
    print '90后'
else:
    print '80后'


#dict
datadict={'key1':1,'key2':2,'key3':3}
print datadict['key3']

if('key4' in datadict):
    print datadict['key4']
else:
    print 'key4不在datadict中'

if('key1' in datadict):
    print 'key1 在datadict中' 
    
#key不存在 返回None 或者指定默认值
print datadict.get('key1')
print datadict.get('dict')==None
print datadict.get('key4',-1)


#set 
#set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key
s=set([1,2,3])
print s

s.add(4)
print s

s.remove(3)
print s

#set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作
s1=set([1,2,3])
s2=set([2,3,4])
print s1&s2
print s1|s2

#字符串不可变
a='abc'
b=a.replace('a','A')
print a
print b


#函数

#定义函数
def function(x):
    if(x>=0):
        return x
    else:
        return -1

#空函数
def empty():
    pass
if(age>19):
    pass

#参数检查
def checkargument(x):
    if(not isinstance(x,(int,float))):
        #raise TypeError('参数类型不是int或者float')
        print '参数类型不是int或者float'

checkargument('111')

#函数返回多个返回值
#返回值是一个tuple！但是，在语法上，返回一个tuple可以省略括号，而多个变量可以同时接收一个tuple，按位置赋给对应的值，所以，Python的函数返回多值其实就是返回一个tuple，但写起来更方便。
def getxy(x,y):
    return x+1,y+1

x,y=getxy(100,200)
print x
print y


#切片
datalist=[1,2,3,4,5]
print datalist[0:3]
print datalist[:3]
print datalist[1:3]
#倒数第一个元素的索引是-1
print datalist[-2:];
print datalist[-2:-1];

datalist=range(100)
#每隔五个取一个
print datalist[::5];

datatuple=(1,2,3,4,5)
print datatuple[:3]


#迭代
d={'a':1,'b':2}
for key in d:
    print key

for key in d.iterkeys():
    print key

for value in d.itervalues():
    print value

for k,v in d.iteritems():
    print k
    print v

#判断一个对象是否可以迭代
from collections import Iterable
print isinstance('123',Iterable)
print isinstance([1,2,3],Iterable)
print isinstance((1,2,3),Iterable)
print isinstance(1,Iterable)

#list变成下标循环
for i,value in enumerate(['a','b']):
    print i,value

print  [x * x for x in range(1, 11)]

print [x * x for x in range(1,10) if x%2==0]

print [x+y for x in 'ABC' for y in 'XYZ']

print [x+y for x in [1,2,3] for y in [4,5,6]]

#文件
import os
print [ d for d in os.listdir('.')]