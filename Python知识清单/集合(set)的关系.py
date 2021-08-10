a={10,20,30,40,50}
b={50,40,30,20,10}
c={10,20,30}
d={'xiaom',80}
e={'xiaom',60}
print(a==b)                #True
print(b.issubset(a))       #True
print(a.issuperset(b))     #True
print(c.isdisjoint(a))     #False
print(d.isdisjoint(e))     #False
                       
#集合是否相等，只与内容有关，与顺序无关
#b .issubset(a)    判断b是不是a的子集吗
#a .issuperset(b)  判断a是不是b的超集吗
#a .isdisjoint(b)    判断a和b有没有交集
