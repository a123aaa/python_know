import os
filename='student.txt'
def main():
    while True:
          menu()
          choice=int(input('请选择执行序号'))
          if choice in [0,1,2,3,4,5,6,7]:
              if choice==0:
                  answer=input('确定退出吗(y/n)')
                  if answer=='y' or answer=='Y':
                      print('感谢使用!!!')
                      break
                  else:
                      continue
              elif choice==1:
                   insert()
              elif choice==2:
                   search()
              elif choice==3:
                  delete()
              elif choice==4:
                  modify()
              elif choice==5:
                  sort()
              elif choice==6:
                  total()
              elif choice==7:
                  show()
              else:
                  break            
def menu():
    print('------------学生系统------------')
    print('         1.录入学生信息')
    print('         2.查找学生信息')
    print('         3.删除学生信息')
    print('         4.修改学生信息')
    print('         5.排列学生信息')
    print('         6.统计学生信息')
    print('         7.显示学生信息')
    print('         0.退出学生系统')
def insert():
    student_list=[]
    while True:
        ID=input('学生ID(1001)：')
        if not ID:
            break
        NAME=input('学生姓名：')
        if not NAME:
            break
        try:
            English=int(input('输入英语成绩：'))
            Python=int(input('输入Python成绩：'))
            Java=int(input('输入Java成绩：'))
        except:
            print('请输入整形成绩')
            continue
        student={'学生姓名':NAME,'ID':ID,'英语成绩':English,'Python成绩':Python,'Java成绩':Java}
        student_list.append(student)
        answer=input('是否继续添加(y/n)')
        if answer=='y' or answer=='Y':
           continue
        else:
           break
    save(student_list)
    print('学生信息以录入')
def save(lst):
    try:
        stu_txt=open(filename,'a',encoding='utf-8')
    except:
         stu_txt=open(filename,'w',encoding='utf-8')
    for item in lst:
        stu_txt.write(str(item)+'\n')
    stu_txt.close()
def search():
    student_query=[]
    while True:
          id=''
          name=''
          if os.path.exists(filename):
              mode=input('1--姓名查找   2--ID查找\n')
              if mode=='1':
                  name=input('请输入学生姓名：')
              elif mode=='2':
                  id=input('请输入学生ID：')
              else:
                  print('输入有误')
                  search()
          with open(filename,'r',encoding='utf-8') as rfile:
                student=rfile.readlines()
                for item in student:
                    d=dict(eval(item))
                    if id!='':
                        if d['ID']==id:
                            student_query.append(d)
                    elif name!='':
                        if d['学生姓名']==name:
                           student_query.append(d)
          show_student(student_query)
          student_query.clear()
          answer=input('是否继续查询(y/n)')
          if answer=='y' or answer=='Y':
                continue
          else:
                break 
    else:
          print('暂无学生信息')
          return
def show_student(lst):
    if len(lst)==0:
        print('无学生信息')
        return
    format_title='{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^8}'
    print(format_title.format('姓名','ID','英语成绩','Python成绩','Java成绩','总成绩'))
    format_data='{:^6}\t{:^12}\t{:^8}\t{:^8}\t{:^8}\t{:^8}'
    for item in lst:
        print(format_data.format(item.get('学生姓名'),
                                 item.get('ID'),
                                 item.get('英语成绩'),
                                 item.get('Python成绩'),
                                 item.get('Java成绩'),
                                 int(item.get('英语成绩'))+int(item.get('Python成绩'))+int(item.get('Java成绩'))
                                 ))
def delete():
    while True:
          student_id=input('请输入需要删除的学生ID：')
          if student_id!='':
              if os.path.exists(filename):
                  with open(filename,'r',encoding='utf-8') as file:
                      student_old=file.readlines()
              else:
                  student_old=[]
              flag=False
              if student_old:
                  with open(filename,'w',encoding='utf-8') as wfile:
                      d={}
                      for item in student_old:
                          d=dict(eval(item))
                          if d['ID']!=student_id:
                              wfile.write(str(d)+'\n')
                          else:
                              flag=True
                      if flag:
                          print(f'ID为{student_id}的学生信息以删除')
                      else:
                          print(f'没有找到ID为{student_id}的学生信息')
              else:
                  print('无学生信息')
                  break
              show()
              answer=input('是否继续删除(y/n)')
              if answer=='y' or answer=='Y':
                  continue
              else:
                  break                       
def modify():
    show()
    if os.path.exists(filename):
       with open(filename,'r',encoding='utf-8') as rfile:
            student_old=rfile.readlines()
    else:
        return
    student_id=input('请输入需要修改的学生ID：')
    with open(filename,'w',encoding='utf-8') as wfile:
        for item in student_old:
            d=dict(eval(item))
            if d['ID']==student_id:
                print('已找到学生信息')
                while True:
                    try:
                       d['ID']=input('学生ID(1001)：')
                       d['学生姓名']=input('学生姓名：')
                       d['English']=int(input('输入英语成绩：'))
                       d['Python']=int(input('输入Python成绩：'))
                       d['Java']=int(input('输入Java成绩：'))
                    except:
                        print('输入有误')
                    else:
                        break
                wfile.write(str(d)+'\n')
                print('修改成功！！')
            else:
                wfile.write(str(d)+'\n')
        answer=input('是否继续修改(y/n)')
        if answer=='y' or answer=='Y':
            modify()
def sort():
    if os.path.exists(filename):
        with open(filename,'r',encoding='utf-8') as rfile:
                student_list=rfile.readlines()
                student_new=[]
                for item in student_list:
                    d=dict(eval(item))
                    student_new.append(d)
    else:
        return
    asc_or_desc=input('0--升序    1--降序')
    if  asc_or_desc=='0':
        asc_or_desc_bool=False
    elif asc_or_desc=='1':
        asc_or_desc_bool=True
    else:
        print('输入无效')
        sort()
    student_new.sort(key=lambda x:int(x['英语成绩']),reverse= asc_or_desc_bool)
    show_student(student_new)
def total():
    if os.path.exists(filename):
        with open(filename,'r',encoding='utf-8') as rfile:
                student=rfile.readlines()
                if student:
                    print(f'一共有{len(student)}名学生')
                else:
                    print('无学生信息')
    else:
        print('无学生信息')
def show():
    student_lst=[]
    if os.path.exists(filename):
        with open(filename,'r',encoding='utf-8') as rfile:
                student=rfile.readlines()
                for item in student:
                    student_lst.append(eval(item))
                if  student_lst:
                    show_student(student_lst)
    else:
        print('无学生信息')
if __name__=='__main__':
    main()