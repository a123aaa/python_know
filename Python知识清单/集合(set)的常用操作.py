arr={10,50,60}
print(type(arr))              #<class 'set'>
print(10 in arr)              #True
print(10 not in arr)          #False
arr.add(80)
print(arr)                    #{80, 10, 50, 60}
arr.update((30,70))
print(arr)                    #{70, 10, 80, 50, 60, 30}
arr.remove(30)
print(arr)                    #{70, 10, 80, 50, 60}
arr.discard(50)              
print(arr)                    #{70, 10, 80, 60}
arr.pop()
print(arr)                    #{10, 80, 60}
arr.clear() 
print(arr)                    #set()
#内容 in 集合名 / 内容 not in 集合名    判断元素是否存在
#集合名 . add( 内容 )                   一次只能添加一个
#集合名 . update( (内容) )              一次至少添加一个
#集合名 . update( {内容} )              一次至少添加一个
#集合名 . update( [内容] )              一次至少添加一个
#集合名 . remove( [内容] )              一次只能删一个
#集合名 . discard( [内容] )             一次只能删一个
#集合名 . pop( )                        随机删一个
#集合名 . clear(  )                     全部删掉
