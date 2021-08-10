def jo(num):
    ji=[]
    ou=[]
    for i in num:
        if i%2:
            ji.append(i)
        else:
            ou.append(i)
    return ji,ou
arr=[1,2,3,4,5,6,7,8,9,10]
print(jo(arr))              #(  [1, 3, 5, 7, 9] , [2, 4, 6, 8, 10]  )
#如果函数不需要返回值，return可以省略
#函数的返回值是一个，直接返回类型
#函数的返回值是多个，返回类型是元组

def fun(a,b=30): #b已经有值，所以叫做默认值形参，简称形参
    print(a,b)
fun(100)         #只传一个参数，b采用默认值
fun(20,40)       #只传两个参数，40默认替换30给b

def arr(a,b,*,c,d):
    print(f'a={a}')
    print(f'b={b}')
    print(f'c={c}')
    print(f'd={d}')
arr(a=2,b=3,c=4,d=8)
arr(4,8,c=1,d=2)
#在'*'号之后的参数，必须采用关键字参数传递
