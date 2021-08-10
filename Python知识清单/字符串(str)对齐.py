arr='hello,Python'
print(arr.center(20,'*'))           #****hello,Python****
print(arr.ljust(20,'*'))            #hello,Python********
print(arr.ljust(10))                #hello,Python
print(arr.ljust(20))                #hello,Python       空格
print(arr.rjust(20,'*'))            #********hello,Python
print(arr.rjust(10))                #hello,Python
print(arr.rjust(20))                #            hello,Python
print(arr.zfill(20))                #00000000hello,Python
print(arr.zfill(10))                #hello,Python
#print(-9806,zfill(10))              #0000009806
#字符串名 .center(站位大小，'标志符')     居中对齐，用'标志符'补齐空位
#字符串名 .center(站位大小)               居中对齐，用'空格'补齐空位
#字符串名 .ljust(站位大小，'标志符')      左对齐，用'标志符'补齐空位
#字符串名 .ljust(站位大小)                左对齐，用'空格'补齐空位
#字符串名 .rjust(站位大小，'标志符')      右对齐，用'标志符'补齐空位
#字符串名 .rjust(站位大小)                右对齐，用'空格'补齐空位
#字符串名 .zfill(站位大小)                右对齐,用0补齐空位
