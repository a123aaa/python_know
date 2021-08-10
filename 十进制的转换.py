def fun():
    num=int(input('输入一个十进制数'))
    print(str(num)+'的二进制是'+bin(num))
    print('{0}的二进制是{1}'.format(num,bin(num)))
    print('%s的二进制是%s' % (num,bin(num)))
    print(f'{num}的二进制是{bin(num)}')
    print('---------------------------')
    print(f'{num}的八进制是{oct(num)}')
    print(f'{num}的十六进制是{hex(num)}')
if __name__=='__main__':
    while True: 
           try:
                fun()
                break
           except ValueError:
                 print('输入错误')
