arr=[10,20,'I LOVE YOU']
print(10 in arr)                              #True     #整形就输入整形查询
print(10 not in arr)                          #False    
print(5  in arr)                              #False
print(5  not in arr)                          #True
print('I LOVE YOU' in arr)                    #True     #字符串型就输入字符串查询
print('I LOVE YOU' not in arr)                #False
print('I DONT LOVE YOU' in arr)               #False
print('I DONT LOVE YOU' not in arr)           #True

#用in时没有标点符号
#查询内容 in 列表名
#查询内容 not in 列表名


for item in arr:                              #依次遍历并赋值给变量
    print(item)                               #结果是--10 20 I LOVE YOU

#for 变量名 in 列表名    
#每遍历一次，列表元素就赋值给变量一次，并且是不断向后遍历
