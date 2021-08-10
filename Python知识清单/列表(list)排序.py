#列表名 . sort()                                 达到升序效果，且地址不变
#列表名 . sort( reverse = False )                达到升序效果，且地址不变
#列表名 . sort( reverse = True )                 达到降序效果，且地址不变
#新列表名 = sorted(列表名)                       达到升序效果，地址改变
#新列表名 = sorted(列表名 ,reverse = False )     达到升序效果，地址改变
#新列表名 = sorted(列表名 ,reverse = True )      达到降序效果，地址改变

arr=[60,50,40,30,20,10]
arr.sort()                                       #或者 arr.sort( reverse = False )
print(arr)                                       #[10, 20, 30, 40, 50, 60]
arr=[10,20,30,40,50,60]
arr.sort( reverse = True )
print(arr)                                       #[60, 50, 40, 30, 20, 10]
arr=[98, 54, 40, 20, 10]
new_arr=sorted(arr)                              #new_arr=sorted(arr,reverse = False )
print(new_arr)                                   #[10, 20, 40, 54, 98]
arr=[20,40,10,98,54]
new_arr=sorted(arr,reverse=True)                 #或者new_arr=sorted(arr)
print(new_arr)                                   #[98, 54, 40, 20, 10]
