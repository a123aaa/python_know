class Student:
     name='小明'               #类属性
     age=10                    #类属性
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

#类包含：类属性，实例方法，静态方法，类方法
#类的名字:为一个或多个单词组成，每个单词首字母大写，其余字母小写
#类属性：直接定义在类里的变量。
#实例属性：先有’def __init__(self,变量名1,变量名2···): ’在用‘self.变量名’使用
#实例方法：‘ def arr(self): ’和‘函数体’
#类方法： ‘ @classmethod ’和‘ def app(cls): ’和‘函数体’ 
#静态方法：‘ @staticmethod ’ 和 ‘ def aqq(): ’和‘函数体’
