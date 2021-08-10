#字典遍历
arr={'张三':10,'李四':20,'王五':30}
for i in arr:
    print(i,arr[i],arr.get(i))                #结果是--张三 10 10     李四 20 20      王五 30 30
#for 变量名 in 字典名 :

#字典式
arr=['张三','李四','王五']
app=[20,50,30]
aqq={ arr : app  for arr,app in zip(arr,app)}
print(aqq)                                       #结果是--{'张三': 20, '李四': 50, '王五': 30}
#字典名={键组名 : 值组名 for 键组名 ,值组名  in zip(键组名 , 值组名)}        返回类型是字典型
