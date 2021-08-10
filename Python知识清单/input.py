ARR=input('你有喜欢的人吗？')    #ARRS是一个str型变量,'='将输入函数的结果赋值给变量ARR,input()是一个输入函数,'你有喜欢的人吗？'只是单纯打印出来
print(ARR)                       #输入的内容
a=input('a=')            #输入10
b=input('b=')            #输入20
print(a+b)               #1020         #因为a和b都是str型，+起到连接作用，而不是相加作用
#改法一
a=int(input('a='))          #输入10,a为int型
b=int(input('b='))          #输入20,b为int型
print(a+b)                  #30
#改法二
a=input('a=')               #输入10,a为float型
a=int(a)                    #a的类型已变为int型
b=input('b=')               #输入20,b为float型
b=int(b)                    #b的类型已变为int型
print(a+b)                  #30
#改法三
a=input('a=')               #输入10,a为float型
b=input('b=')               #输入20,b为float型
print(int(a)+int(b))        #30              #ab,b类型不变

#input()---返回值类型是str()型
