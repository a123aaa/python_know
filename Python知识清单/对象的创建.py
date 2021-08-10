#对象的创建又称类的实例化
#语法：实例名=类名()
#一个类可以创建多个实例对象，每个对象的属性值不同
class Student:
     name='肖战'                     #类属性
     age=10                          #类属性
     def __init__(self,sex,like):    #sex和like为实例属性
         self.sex='男'
         self.like='game'
     def arr(self):                  #实例方法
         print(name,age,self.sex,self.like)
     @classmethod
     def app(cls):                  #类方法
         print('类方法')
     @staticmethod                  #静态方法
     def aqq():
         print('静态方法')
stu=Student('小明',20)
print(stu.name)
print(stu.age)

#动态绑定属性和方法
def show():          #方法函数创建
    print('abc')
stu=Student('jack',30)
stu.wife='zzy'       #动态绑定wife属性
print(stu.wife)
stu.show=show        #动态绑定方法
stu.show()

