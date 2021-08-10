#●如果子类对继承自父类的某个属性或方法不满意，可以在子类中对其(方法体)进行重新编写
#●子类重写后的方法中可以通过super().xxx()调用父类中被重写的方法
class Person (object):                                   #定义父类
      def __init__(self,name,age):
          self.name=name
          self.age=age
      def info(self):
          print(f'姓名:{self.name},年龄:{self. age}')
class Student(Person):                                  #定义子类
      def __init__(self,name,age,score):
           super().__init__(name,age)                   #重写
           self. score=score
      def info(self):
           super().info()                                    #重写
           print(f'学号:{self. score}')
stu=Student('Jack',20,'1001')                       #测试
stu.info() 

