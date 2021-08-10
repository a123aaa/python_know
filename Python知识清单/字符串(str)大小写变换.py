arr='aBcDe'
app=arr.swapcase()
print(app)                     #AbCdE
app=arr.upper()
print(app)                     #ABCDE
app=arr.lower()
print(app)                     #abcde
arr='I LOVE YOU'
print(arr.title())             #I Love You
arr='I LOVE YOU'
print(arr.capitalize())        #I love you
#新字符串=字符串 .upper()         把所有字母改为大写
#新字符串=字符串 .lower()         把所有字母改为小写
#新字符串=字符串 .swapcase()      把所有字母的大小写交换
#新字符串=字符串 .capitalize()    把第一个单词的第一个字符改为大写，其他单词都为小写
#新字符串=字符串 .title()         把每个单词的第一个字符转换为大写，把每个单词的其余字符转换为小写
