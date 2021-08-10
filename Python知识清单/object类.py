#●object类是所有类的父类，因此所有类都有object类的属性和方法。
#●内置函数dir()可以查看指定对象所有属性
#●Object有一个__str__()方法， 用于返回一个对于“对象的描述”，对应于内置函数str()经常用于print()方法，帮我们查看对象的信息，所以我们经常会对__str__()进行重写
class Person(object):
      def __init__(self,name,age):
           self.name=name
           self.age=age
      def info(self):
           print(f'姓名:{self. name},年龄:{self. age}') 
      def __str__(self):
           return f'姓名:{self. name},年龄:{self. age}'
o=object()
p=Person('Jack' ,20)
print(dir(o))
print(dir(p))
print(p) 
