arr='hello weord python'
print(arr.split())                            #['hello', 'weord', 'python']
arr='hello|weord|python' 
print(arr.split('|'))                         #['hello', 'weord', 'python']
print(arr.split('|',maxsplit=1))              #['hello', 'weord|python']
print(arr.rsplit('|',maxsplit=1))             #['hello|weord', 'python']

#字符串名 .split()                   从左面开始劈，默认劈分字符是空格，返回值是列表
#字符串名 .split( )                  从左面开始劈，以空格为标志，切割字符串
#字符串名 .split('|')                从左面开始劈，以'|'为标志，切割字符串
#字符串名 .split('*')                从左面开始劈，以'*'为标志，切割字符串
#字符串名 .split('|',maxsplit=a)     从左面开始劈，以'|'为标志，切割字符串,且只识别前a个'|'

#字符串名 .rsplit()                   从右面开始劈，默认劈分字符是空格，返回值是列表
#字符串名 .rsplit( )                  从右面开始劈，以空格为标志，切割字符串
#字符串名 .rsplit('|')                从右面开始劈，以'|'为标志，切割字符串
#字符串名 .rsplit('*')                从右面开始劈，以'*'为标志，切割字符串
#字符串名 .rsplit('|',maxsplit=a)     从右面开始劈，以'|'为标志，切割字符串,且只识别前a个'|'
