arr='hallo,word,word,word'
print(arr.replace('word','python'))              #hallo,python,python,python
print(arr.replace('word','python',2))            #hallo,python,python,word
arr=['hallo','word','word','word']               #arr=('hallo','word','word','word')
print('|'.join(arr))                             #hallo|word|word|word
print(''.join(arr))                              #hallowordwordword
print(' '.join(arr))                             #hallo word word word
print('*'.join('abcd'))                          #a*b*c*d


#字符串名 .replace('被替代的子串','替换串')      用'替换串'替换字符串中所有'被替换的串'
#字符串名 .replace('被替代的子串','替换串',a)    用'替换串'替换字符串中前a个'被替换的串'
#'标志符' .join(字符串名)                        用'标志符'替换字符串的','
#'标志符' .join(字符串)                          用'标志符'替换字符串的','
