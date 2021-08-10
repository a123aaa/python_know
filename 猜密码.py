import random
key=random.randint(0,100)
while True:
    code=int(input('输入数字'))
    if code>key:
        print('猜到了')
    elif code<key:
        print('猜小了')
    elif code==key:
        print('猜对了')
        break
