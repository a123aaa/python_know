for i in range(3):
    print(i)                 #0 1 2
for i in range(-3):
    print(i)                 #无
for i in range(1,5):
    print(i)                 #1 2 3 4 
for i in range(-3,5):
    print(i)                 #-3 -2 -1 0 1 2 3 4
for i in range(-3,-5):
    print(i)                 #无
for i in range(2,8,2):
    print(i)                 #2 4 6
for i in range(2,8,-2):
    print(i)                 #无
print(3 in range(1,5,2))     #True
print(-3 in range(-5,2,2))   #True
print(8 in range(1,8,1))     #False
#range()函数用于创造一个整数序列,返回值是一个迭代器对象
#stop必须大于0，当stop为负时，什么都不打印
#range( stop )                创造一个[0,stop-1]之间的整数序列，步长默认为1.  
#range( start ,stop )         创造一个[start ,stop-1]之间的整数序列，步长默认为1。start可以为负数 
#range( start ,stop ,step)    创造一个[0,stop-1]之间的整数序列，步长为strp  
#range()函数不用时仅仅存储start，stop，step三个参数，只有当参与计算时才有相关元素
#可以用 in 和 not in 判断整数序列是否存在
