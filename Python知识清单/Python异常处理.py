try:
    a=int(input('被除数'))
    b=int(input('除数'))
    result=a/b
except ZeroDivisionError:     #不符合就判断下一级，符合下一级就不执行
    print('除数不能为0')
except ValueError:            #不符合就判断下一级，符合下一级就不执行
    print('必须输入整数')     
else:                         #上面两个都不符合，就执行这个
    print(result)
finally:                      #无论上面是否执行，这个都都执行
    print('无论是否出错都执行')
