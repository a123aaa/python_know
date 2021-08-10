#and运算：都真才真，一假全假，返回值是布尔类型
a=1
b=2
print(a==1 and b==2)         #True
print(a!=1 and b==2)         #False
print(a==1 and b!=2)         #False
print(a!=1 and b!=2)         #False

#or运算：有真则真，全假才假，返回值是布尔类型
a=1
b=2
print(a==1 or b==2)          #True
print(a!=1 or b==2)          #True
print(a==1 or b!=2)          #True
print(a!=1 or b!=2)          #False

#not运算：对布尔类型取反，返回值是布尔类型
a=1
b=True
c=False
print(not a==1)              #False
print(not a!=1)              #True
print(not b)                 #False
print(not c)                 #True

#in 和 not in运算：字符或字符串是否在字符串里，返回值是布尔类型
arr='abcdef'
print('a' in arr)            #True
print('a' not in arr)        #False
print('h' in arr)            #False
print('h' not in arr)        #True
print('ab' in arr)           #True
print('ab' not in arr)       #False
