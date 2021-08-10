class Person (object):                                   #定义父类
      def __init__(self, name, age):
          self.name=name
          self.age=age 
      def info(self):
          print(f'姓名:{self. name},年龄:{self. age}')
class Student(Person):                                   #定义子类
      def __init__(self,name,age,score):
          super().__init__(name, age)
          self.score=score
stu=Student('Jack',20,'1001' )                        #测试
stu.info() 

