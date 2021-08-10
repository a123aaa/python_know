#列表的添加 
arr=[10,20,'I LOVE YOU']
arr2=['I LOVE YOU','YES']
arr3=[1,2,3,4,5,6]
arr4=[99]
arr.append(30)                    #或者arr.extend(30)                                
print(arr)                        #[10, 20, 'I LOVE YOU', 30]
arr.append('yes')                 #或者arr.extend('yes')               
print(arr)                        #[10, 20, 'I LOVE YOU', 30, 'yes']
arr.append(arr2)                  #添加一个列表，并将一个列表作为一个元素
print(arr)                        #[10, 20, 'I LOVE YOU', 30, 'yes', ['I LOVE YOU', 'YES'] ]
arr.extend(arr2)                  #添加一个列表，并将一个列表作为多个元素               
print(arr)                        #[10, 20, 'I LOVE YOU', 30, 'yes', ['I LOVE YOU', 'YES'], 'I LOVE YOU', 'YES']
arr2.insert(1,30)                 #在索引为1的位置添加30
print(arr2)                       #['I LOVE YOU', 30, 'YES']
arr[1:5]=arr2                     #arr列表的[1,5-1]的元素全部删掉，arr2列表的所以元素从start开始存，直到全部存完
print(arr)                        #[10, 'I LOVE YOU', 30, 'YES', ['I LOVE YOU', 30, 'YES'], 'I LOVE YOU', 'YES']
arr[1:2]=arr3                       
print(arr)                        #[10, 1, 2, 3, 4, 5, 6, 30, 'YES', ['I LOVE YOU', 30, 'YES'], 'I LOVE YOU', 'YES']
arr[1:5]=arr4
print(arr)                         #[10, 99, 5, 6, 30, 'YES', ['I LOVE YOU', 30, 'YES'], 'I LOVE YOU', 'YES']
#列表名 . append(添加内容)              将添加内容作为一个元素添加到最后位置
#列表名 . extend(添加内容)              将添加内容作为多个元素添加到最后位置
#列表名 . insert(添加位置，添加内容)    将添加内容作为一个元素添加到指定位置位置
#列表名 [start,stop]=另外一个列表       列表的[stsrt,stop-1]的元素全部删掉，另外一个列表的所以元素从start开始存，直到全部存完


#列表的删除
arr=[ 10 , 20 , ' I LOVE YOU ' ]
print(id(arr))
arr.remove(20)                         #将元素20删除，如后面还有就删除第一个
print(arr)                             #[10, 'I LOVE YOU']
arr.pop(0)                             #将索引为一的元素删掉
print(arr)                             #[ 'I LOVE YOU']

arr=[20,30,40,50,60]
arr[1:3]=[]                            #将索引为1和2的删掉
print(arr)                             #[20, 50, 60]    
arr.clear()                            #清除列表所以内容
print(arr)                             #[]
del arr                                #删掉列表
print(arr)                             #结果是--name 'arr' is not defined     
#列表的删减操作都不会改变列表的地址，del除外
#列表名 .remove(删除内容)        列表储存位置不变，一次只删一个元素，重复元素只删第一个
#列表名 .pop(索引位置)           列表储存位置不变，删索引位置元素，若不指明索引位置则默认删掉最后一个元素
#列表名 [stsrt , stop]=[]        让列表[strrt,stop-1]内容为空，起到删除的效果
#列表名 .clear()                 清除列表所以内容
#del  列表名                     删掉列表，是列表不存在


#列表的修改
arr=[ 20,30,40,50,60 ]
arr1=[65,75,85]
arr[2]=100                              #将索引为2的元素改为100
print(arr)                              #[20, 30, 100, 50, 60]
arr[1:3]=[ 100,200,300,400 ]            #将索引为1和2的元素删掉，再从索引1处开始添加100,200,300,400
print(arr)                              #[20, 100, 200, 300, 400, 50, 60]
arr[1:2]=arr1                           #将索引为1元素删掉，再从索引1处开始添加arr1
print(arr)                              #[20, 65, 75, 85, 200, 300, 400, 50, 60]
#列表名 [索引]=新元素
#列表名 [start : stop]=另一个列表       将[start:stop-1]的元素删掉再从索引start处开始添加另一个列表
#列表名 [start : stop]=[内容]           将[start:stop-1]的元素删掉再从索引start处开始添加另一个列表