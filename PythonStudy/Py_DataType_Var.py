print 'i am ���»�'
print "i'am ��ѧ��"
print 'i\'am \"����'
print 'i \'am \n���»�'
print 'i \'am \\ ���»�'

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
    print '����'
else:
    print 'δ����'


#����
var_1=1
var_2='1'
Flag=True

a='abc'
b=a
a='xyz'
print b

#����
PI=3.1415926

print 10/3
print 10.0/3
print 10%3

#Pythond�ַ���
#Python�ṩ��ord()��chr()���������԰���ĸ�Ͷ�Ӧ�������໥ת��
print ord('A')
print chr(65)

#Python�����Unicode��֧�� Unicode��ʾ���ַ�����u'zifuchuan'��ʾ
print u'����'.encode('utf-8')
print '����'
print 'abc'.decode('utf-8')
print u'����'.encode('utf-8')

#�ַ����ĳ���
print len('ab')
print len(u'����')

#��ʽ��
print 'Hello,%s' % 'world'

print 'Hello,%s,��������%d' % ('����',10000000)

#list
datalist=['����','����']
print datalist
print len(datalist)
print datalist[0]
print datalist[1]

print datalist[len(datalist)-1]
print datalist[-1]
print datalist[-2]

datalist.append('����')
print datalist[-1]

#ɾ��ĩβ��Ԫ��
datalist.pop()
print datalist
#ɾ��ָ��λ�õ�Ԫ��
datalist.pop(0)
print datalist
#�滻ĳ��λ�õ�Ԫ��
datalist[0]='liudehua'
print datalist

#list���������Ϳ��Բ�ͬ
datalist=['liudehua',1,True,['data',True]]
print datalist

datalist=[]
print datalist
print len(datalist)

#tuple Ԫ��
datatuple=('1','2')
print datatuple;
print datatuple[0]

datatuple=(1)#���Ǹ�����
print datatuple
datatuple=(1,)#���Ǹ�����
print datatuple

#tuple���ܱ���ָ����ÿ��Ԫ�ص�ָ���ܱ� ������������ݿɱ�
datatuple=('a','b',['c','d'])
datatuple[2][0]='wo change'
datatuple[2][1]='wo bian'
print datatuple


#�����ж�
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


#ѭ��
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
birth=raw_input('������������䣺')
if(birth>1990):
    print '90��'
else:
    print '80��'
birth=int(raw_input('������������䣺'))
if(birth>1990):
    print '90��'
else:
    print '80��'


#dict
datadict={'key1':1,'key2':2,'key3':3}
print datadict['key3']

if('key4' in datadict):
    print datadict['key4']
else:
    print 'key4����datadict��'

if('key1' in datadict):
    print 'key1 ��datadict��' 
    
#key������ ����None ����ָ��Ĭ��ֵ
print datadict.get('key1')
print datadict.get('dict')==None
print datadict.get('key4',-1)


#set 
#set��dict���ƣ�Ҳ��һ��key�ļ��ϣ������洢value������key�����ظ������ԣ���set�У�û���ظ���key
s=set([1,2,3])
print s

s.add(4)
print s

s.remove(3)
print s

#set���Կ�����ѧ�����ϵ���������ظ�Ԫ�صļ��ϣ���ˣ�����set��������ѧ�����ϵĽ����������Ȳ���
s1=set([1,2,3])
s2=set([2,3,4])
print s1&s2
print s1|s2

#�ַ������ɱ�
a='abc'
b=a.replace('a','A')
print a
print b


#����

#���庯��
def function(x):
    if(x>=0):
        return x
    else:
        return -1

#�պ���
def empty():
    pass
if(age>19):
    pass

#�������
def checkargument(x):
    if(not isinstance(x,(int,float))):
        #raise TypeError('�������Ͳ���int����float')
        print '�������Ͳ���int����float'

checkargument('111')

#�������ض������ֵ
#����ֵ��һ��tuple�����ǣ����﷨�ϣ�����һ��tuple����ʡ�����ţ��������������ͬʱ����һ��tuple����λ�ø�����Ӧ��ֵ�����ԣ�Python�ĺ������ض�ֵ��ʵ���Ƿ���һ��tuple����д���������㡣
def getxy(x,y):
    return x+1,y+1

x,y=getxy(100,200)
print x
print y


#��Ƭ
datalist=[1,2,3,4,5]
print datalist[0:3]
print datalist[:3]
print datalist[1:3]
#������һ��Ԫ�ص�������-1
print datalist[-2:];
print datalist[-2:-1];

datalist=range(100)
#ÿ�����ȡһ��
print datalist[::5];

datatuple=(1,2,3,4,5)
print datatuple[:3]


#����
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

#�ж�һ�������Ƿ���Ե���
from collections import Iterable
print isinstance('123',Iterable)
print isinstance([1,2,3],Iterable)
print isinstance((1,2,3),Iterable)
print isinstance(1,Iterable)

#list����±�ѭ��
for i,value in enumerate(['a','b']):
    print i,value

print  [x * x for x in range(1, 11)]

print [x * x for x in range(1,10) if x%2==0]

print [x+y for x in 'ABC' for y in 'XYZ']

print [x+y for x in [1,2,3] for y in [4,5,6]]

#�ļ�
import os
print [ d for d in os.listdir('.')]