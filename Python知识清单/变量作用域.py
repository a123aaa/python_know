name='小鲁'     #全局变量
print(name)     #小鲁
def arr():
   i=1          #局部变量
   print(i)     #1
   print(name)  #小鲁
def app():
    global i    #局部变全局
    i=2
    print(i)   #2
arr()     
app()
print(i)       #2

#全局变量：定义在函数外，作用域在它下面的所有地方
#局部变量：定义在函数内，作用域在函数体内
#局部变全局：global  变量名  ,作用域在它下面的所有地方 
