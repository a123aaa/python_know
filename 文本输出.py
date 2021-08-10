#用print输出
fp=open('E:/python1.txt','a')
print('再也回不去了',file=fp)
fp.close()

#直接输出
with open('E:/python1.txt','a') as file:
    file.write('你不再回来')

