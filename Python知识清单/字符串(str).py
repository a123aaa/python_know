print('hello\nworld')   #\n表示换行
print('hello\tworld')   #\t表示用空格占位，空格数==4-前面字符数%4。（当空格数为0时，重新开辟四字节空间）
print('hello\rworld')   #\r表示后面单词的字符一个一个替换前面单词字符
print('hello\bworld')   #\b用后面单词第一字符压在前面单词第一字符上
print(r'hello\bword')   #r+字符串使串内字符失效
