#字典查找，修改，增删
arr={'时':100,'点':200,'分':50}
print('时' in arr)                     #True
print('时' not in arr)                 #False
del arr['时'] 
print(arr)                             #{'点': 200, '分': 50}
arr.clear()
print(arr)                             #{}
arr['分钟']=99
print(arr)                             #{'分钟': 99}
arr['分钟']=100
print(arr)                             #{'分钟': 100}
#用 '键' in 字典名  或  '键' not in 字典名     判断该键在字典中是否存在      
#用 del 字典名[ '键名']                        删除该键
#用 字典名.clear()                             清空该字典
#字典名[ ' 键名 ' ]=值                         该键存在则修改键的值，不存在就添加该键，并给值


#字典视图
arr={'小鲁':18,'小鑫':50,'小明':80}
print(arr.keys())                #dict_keys(['小鲁', '小鑫', '小明'])
print(arr.values())              #dict_values([18, 50, 80])
print(arr.items())               #dict_items([('小鲁', 18), ('小鑫', 50), ('小明', 80)])
#新字典名=字典名 .keys()        得到字典所以的键，返回类型是dict_keys
#新字典名=字典名 .values()      得到字典所以的值，返回类型是dict_values
#新字典名=字典名 .items()       得到字典所以的值，返回类型是dict_items
