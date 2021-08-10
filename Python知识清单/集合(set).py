#集合的创建
#集合名={ 内容，内容，···  }           集合元素不能重复，否则被替代
#集合名=set( range[内容] )
#集合名=set( range(内容) )
#集合名=set( range('字符串'))
#集合名=set( {内容···} )
#集合名=set(())
#元素排列不安顺序

#集合式
arr={i*i*i for i in range(1,5)}
print(arr)                            #结果是-- {8, 1, 27, 64}
#集合名= {含变量的表达式   for  变量名   in   range(start ,stop )}
