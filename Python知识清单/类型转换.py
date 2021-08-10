#其他类型用str()转换成str类型
name='小鲁'
age='20'
print('我是'+name+'今年'+str(age)+'岁了')       #我是小鲁今年20岁了       #print('我是'+name+'今年'+age+'岁了')是错的，因为整形(int)不能和字符串型(str)相加
a=1
b=3.14
c=True
print(type(a),type(b),type(c))                  #<class 'int'> <class 'float'> <class 'bool'>
print(type(str(a)),type(str(b)),type(str(c)))   #<class 'str'> <class 'str'> <class 'str'>
print(type(a),type(b),type(c))                  #<class 'int'> <class 'float'> <class 'bool'>   及转换类型后，其本身类型仍然不变
#强制类型转换后，其本身类型仍然不变
#int,float和bool类型都可以转换成str类型

#其他类型用int()转换成int类型
print(int('123'))        #结果是--123            前提是字符串是数字串，并且是整数类型
print(int('123.4'))      #报错，
print(int('abc'))        #报错，
print(int(123,4))        #结果是--123          转换成int型后只保留整数部位
print(int(True))         #结果是--1

#其他类型用float()转换成float类型
print(float('123'))      #123.0，          #字符串是数字类型就可以，会整数型加'0'
print(float('123.4'))    #123.4，          #字符串是数字类型就可以，浮点型型不变
print(float('abc'))      #报错
print(float(123))        #123.0，          #整形变浮点型加'0'
print(float(True))       #1.0
