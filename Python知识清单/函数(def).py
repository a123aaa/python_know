#创建函数
def arr(a,b):
    return a-b
print(arr(10,20))          #-10     #位置实参
print(arr(20,10))          #10      #位置实参
print(arr(a=10,b=20))      #-10     #关键字实参
print(arr(a=20,b=10))      #10      #关键字实参

'''def  函数名 ([输入参数]):
        函数体
        [return xxx]'''
#位置实参：根据形参对应的位置进行传参
#关键字实参：根据形参名称进行实参传递

#函数传参
def change(new_a,new_b):
    print('2-------')                  #2-------
    print(f'new_a={a}',id(new_a))      #new_a=11              9400608
    print(f'new_b={b}',id(new_b))      #new_b=[10, 20, 30]    55309320
    new_a=100
    new_b.append(40)
    print('3-------')                  #3-------
    print(f'new_a={a}',id(new_a))      #new_a=11                 9402032
    print(f'new_b={b}',id(new_b))      #new_b=[10, 20, 30, 40]   55309320
   
a=11
b=[10,20,30]
print('1------')          #1------
print(f'a={a}',id(a))     #a=11                9400608
print(f'b={b}',id(b))     #b=[10, 20, 30]      55309320
change(a,b)
print('4-------')         #4-------
print(f'a={a}',id(a))     #a=11                 9400608
print(f'b={b}',id(b))     #b=[10, 20, 30, 40]   55309320
#参数传递的是不可变对象，在函数体修改后 原参数值和地址都不变，函数体参数值不变，地址改变
#参数传递的是可变对象，在函数体修改后 原参数值改变，地址都不变， 函数体参数值改变，地址改变