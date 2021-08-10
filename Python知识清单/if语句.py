#单分支if
num=100
money=int(input('请输入取款金额'))         #将输入的值赋给money
if money<=num:                             #if  条件语句  ':'
   num-=money                              #缩进格式要对齐
   print('取款成功，余额为',num,'元')      #缩进格式要对齐
else:                                      #else+:
   print('取款失败，你只有',num,'元')      #缩进格式要对齐

#多分支if
score=int(input('请输入一个成绩'))       #当有一条语句被执行时，后面语句不在执行
if   score>=90 and score<=100:           #或if   90<=score<=100:
   print('优秀')
elif score>=80 and score<90:             #或elif 80<=score<90:
   print('不错')
elif score>=70 and score<80:             #或elif 70<=score<80:
   print('一般')
elif score>=60 and score<70:             #或elif 60<=score<70:
   print('合格')
elif score>=0 and score<60:              #或elif  0<=score<60:
   print('不合格')
else:
   print('输入成绩无效')

#嵌套if
answer=input('你是会员吗（是/否）')
if answer=='是':                   #if语句内的语句被执行，后面的elif和else不在执行
   money=int(input('购物金额'))
   if money>200:
      print('打九折')
   else:
      print('打八折')
elif answer=='否':
      print('不打折')
else:
      print('输入错误')

#条件表达式
a=int(input('a='))
b=int(input('b='))
print('a>b' if  a>b  else  'a<=b')   #如果a>b为真，则打印a>b,否则打印  a<=b
