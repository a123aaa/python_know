arr='hello,python'
print(arr.isidentifier())              #False
print('hello_python'.isidentifier())   #True
print('hello_123'.isidentifier())      #True
print(arr.isalpha())                   #False
print('aAbB'.isalpha())                #True
# .isidentifier()   判断指定的字符串是不是合法的标识符（由字母，数字（不能放在开头），下划线）
# .isspace()        判断指定的字符串是否全部由空白字符组成（回车，换行，水平制表符）
# .isalpha()        判断指定的字符串是否全部由字母组成
# .isdecimal()      判断指定的字符串是否全部由十进制的数字组成
# .isnumeric()      判断指定的字符串是否全部由数字组成(可以有阿拉伯数字)
# .isalnum()        判断指定的字符串是否全部由字母和数字组成