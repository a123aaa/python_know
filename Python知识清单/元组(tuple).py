arr=('I LOVE YOU','YES',20,10)          
aqq='I LOVE YOU','YES',20,10           
app=tuple(('I LOVE YOU','YES',20,10))
ayy='yes',                              #','不能少
print(arr)                              #('I LOVE YOU', 'YES', 20, 10)
print(aqq)                              #('I LOVE YOU', 'YES', 20, 10)
print(app)                              #('I LOVE YOU', 'YES', 20, 10)
print(ayy)                              #('yes',)
#元组名=( 内容 )= 内容 = tuple((内容))        小括号可以省略不写。当内容只要一个时，需要在后面加 ' , '否则会被认为是字符串


for app in arr:                                #对元组进行遍历
    print(app)
