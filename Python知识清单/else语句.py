car=input('你是否有会员(是/否)')
while car=='是':
    money=int(input('消费金额'))
    if money>200:
        print('打六折')
        break
    else:
        print('不打折')
else:
     print('谢谢光临')


for money in range(3):
    money=int(input('消费金额'))
    if money>200:
        print('打六折')
        break
    else:
        print('不打折')
else:
     print('谢谢光临')
'''if ··· :
      ···
   else :
      ···
''' #if条件表达式不成立就立刻执行else。反之则不执行else

'''while ··· :
         ···
   else:
         ···
''' #while里的break表达式没有执行，退出while后，就执行else。反正之不执行else

'''for ···in  ··· :
         ···
   else:
         ···
''' #for里的break表达式没有执行，退出while后，就执行else。反正之不执行else
