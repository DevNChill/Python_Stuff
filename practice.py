# vowel=cons=0
# f=open('demo.txt','w+')
# user_input=input('Enter whatever you want to store in the file')
# f.write(user_input)
# f.seek(0)
# data=f.read()
# print(str(data))
# l=data.split()
# print(l)
# length=len(l)
# for i in range(length):
#     word=l[i]
#     for char in word:
#         if char.lower() in 'aeiou':
#             vowel+=1
#         else:
#             cons+=1
# print(f'total no of vowels are {vowel} and total no of cons are {cons}')
# spaces=len(l)-1
# print(f'Total no of spaces in the file is {spaces}')
# f.close()
# import pickle
# f=open('demo.dat','rb')
# data=input('Enter your input')
# pickle.dump(data,f)
# print(pickle.load(f))
# import csv
# def write ():
#     with open('demo.csv','w') as fobj:
#         f=csv.writer(fobj)
#         f.writerow(['Roll','Name','Marks'])
#         while True:
#             roll=int(input('Enter your roll no: '))
#             name=input('Enter your name: ')
#             marks=int(input('Enter your marks: '))
#             data=[roll,name,marks]
#             f.writerow(data)
#             choice=int(input('1 ->Enter More\n2 -> No more\n3 ->Enter Your Choice: '))
#             if choice == 2:
#                 break
#         print('File succesfully created')
# write()
# import csv
# def read():
#     with open('demo.csv','r') as fobj:
#         f=csv.reader(fobj)
#         for i in f:
#             print(i)
# read()
# print(2*'*')
import mysql.connector as c
con = c.connect(host='localhost',user='root',passwd='groot',) #used to connect mysql and python and return a connection object
cur = con.cursor() # allows to execute sql commands in python
cur.execute('create database if not exists sakilla')
cur.execute('use sakilla')
cur.execute('create table if not exists student(roll integer primary key, name varchar(20) NOT NULL, marks integer)')
con.commit()
try:
    while True:
        choices=int(input('1 -> data insert\n2 ->data retrieve\n3 -> data update\n4 ->data delete\n5 ->Display all data\n6 ->Exit\n  ->Enter your choice : '))
        if choices==1: # insert data
            roll=int(input('Enter your roll no : '))
            name=(input('Enter your Name : '))
            marks=int(input('Enter your marks : '))
            cur.execute("insert into student values({} ,'{}', {})".format(roll , name , marks))
            con.commit()
            print('row inserted succesfully!')
        elif choices ==2: #retrieve data
            roll=int(input("Enter roll no to find : "))
            cur.execute("Select * from student where roll={}".format(roll))
            data=cur.fetchone()
            if cur.rowcount == 0:
                print('Roll no not found')
            else:
                print(data)
        elif choices == 3: # update data
            roll=int(input("Enter roll to update"))
            marks=int(input('Enter Updated marks'))
            cur.execute("update student set marks={} where roll={}".format(marks,roll))
            con.commit()
            data=cur.fetchone
            if data == 0:
                print('Roll not found')
            else:
                print('Data updated succesfully')
        elif choices == 4: # delete data
            roll=int(input('Enter roll to delete'))
            cur.execute("delete from student where roll={}".format(roll))
            data=cur.fetchone
            con.commit()
            if cur.rowcount == 0:
                print('Roll not found')
            else:
                print('Deleted Succesfully')
        elif choices == 5: # Display all data
            cur.execute('select * from student')
            con.commit()
            data=cur.fetchall
            if cur.rowcount == 0:
                print('Empty set')
            else:
                for i in data:
                    print(i)
        elif choices == 6:
            break
        else:
            print('Invalid Choice !! Please enter again')
except Exception :
    print('Invalid Error')
# def get_input():        
#     a = []
#     size = int(input("Enter the size of the list : "))
#     for i in range(size):
#         value = int(input('Enter the number : '))
#         a.append(value)
#     print(f"The list is {a}")
#     return a
# list = get_input()
# print(list)
# def push(list,element):
#     list.append(element)
#     print(f"The final stack is {list}")

    
# def pop(list):
#         p = list.pop()
#         print(f"The element removed is {p}")
#         print(f"The final stack is {list}")

# def seek(list):
#     print(f"The last element of stack is {list[-1]}")
# while True:
#     choice = int(input("1 ->push\n2 ->pop\n3 -> seek\n4 ->Exit()\nEnter your choice : "))
#     if choice == 1:
#         element = int(input("Enter the element you want to push : "))
#         push(list,element)
#     elif choice == 2:
#         if len(list)==0:
#             print('Stack Underflow')
#         else:
#             pop(list)
#     elif choice == 3:
#         seek(list)
#     elif choice == 4:
#         break


