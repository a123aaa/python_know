arr=['I','LOVE','YOU',99]             #列表名=[ '内容一 ','内容二'····]
print(type(arr))                      #<class 'list'>
print(arr)                            #['I', 'LOVE', 'YOU', 99]       #打印列表全部内容
print(arr.index('LOVE'))              #1                              #用index()查找内容,并且从0开始递增查询，查到就停止
print(arr.index('LOVE',1,4))          #1                              #用index()查找内容，且查找范围是[1,4-1]
print(arr[1])                         #LOVE
print(arr[-1])                        #99
#用 列表名.index('查找内容'),从0开始递增查询，查到就停止
#用 列表名.index('查找内容',start,stop),从start开始递增查询，查到stop-1就停止
#'I','LOVE','YOU',99分别存放在空间1,2,3,4中，而这1,2,3,4有存放在空间a中，而arr的值就是a

#    -7 -6 -5 -4 -3 -2 -1:负索引
arr=[10,20,30,40,50,60,70]
#    0  1  2  3  4  5  6 :正索引
print(arr[1:7:1])           #[20, 30, 40, 50, 60, 70]    #[start : stop : step]，start默认是0，stop默认是最后一个对象，step默认步长为1。打印范围是[start , stop-1]
print(id(arr))              #62611336
print(id(arr[1:7:1]))       #75612552                    #取部分，地址也会改变
print(arr[-2:-7:-1])        #[60, 50, 40, 30, 20]        #步长为负数时，70就是打印的起点，10是终点   
print(arr[6:0:-1])          #[70, 60, 50, 40, 30, 20]    #正索引6对应负索引-1为起点，正索引0对应负索引-7为终点
#列表元素按顺序有序排列，索引映射唯一数据，列表可以储存重复数据，任意数据类型混存，根据需要动态分布和回收内存

#列表生成式 
arr=[i*i*i for i in range(1,5)]
print(arr)                             #[1, 8, 27, 64]
arr=[3*i for i in range(6,16)]
print(arr)                             #[18, 21, 24, 27, 30, 33, 36, 39, 42, 45]
#列表名=[ 含变量的表达式 for 变量名  in  range( start , stop )]

