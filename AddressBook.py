#!/usr/bin/env python
#-*-coding:utf-8-*-

import cPickle as p
import shutil
import fileinput
from prettytable import PrettyTable
import re
import os
import sys

def using():
    print '''
    +--------------------------------+
    |       通讯簿管理系统 v0.1      |
    |--------------------------------|
    |       1)  添加纪录             |
    |       2)  删除记录             |
    |       3)  更改记录             |
    |       4)  查询记录             |
    |                                |
    |       5)  退出程序             |               
    +--------------------------------+
    '''
if not os.path.exists('./.data.pkl'):
        os.system('touch ./.data.pkl')

def intofile(list_name):
    file_pkl = open('./.data.pkl','r+')
    p.dump(list_name,file_pkl)
    file_pkl.close()

def loadfile():
    load_pkl= open('./.data.pkl') 
    global AddDict
    if len(load_pkl.read()) == 0:
        AddDict = {}
        load_pkl.close()
    else:
        load_pkl= open('./.data.pkl')
        AddDict = p.load(load_pkl)
        load_pkl.close()

def showtable(name):
    global a
    a = PrettyTable(["姓名","英文名","部门","分机号","手机号","邮箱"])
    a.align["姓名"] = "l"
    a.add_row([name, AddDict[name][0], AddDict[name][1], AddDict[name][2], AddDict[name][3], AddDict[name][4] ])
    print a

def add():
    loadfile()
    while True:
        name = raw_input('姓名：').strip()
        if AddDict.has_key(name):
            print "姓名已存在，请重新输入！"
            continue
        ename = raw_input('英文名：').strip()
        department = raw_input('部门：').strip()
        tel = raw_input('分机号：').strip()
        mobile = raw_input('手机号：').strip()
        mail = raw_input('邮箱：').strip()
        AddDict[name] = [ename,department,tel,mobile,mail]
        showtable(name)
        Confirm = raw_input("确认信息：[y/n]: ").strip()
        if Confirm == "y":
            intofile(AddDict)
            print "添加成功！"
            break
        else:
            print "取消操作，请重新添加！"
            break
def delete():
    loadfile()
    while True:
        delete_name = raw_input('输入要删除的姓名(q:返回)：').strip()
        if len(delete_name) == 0: continue
        if delete_name == 'q': break
        if AddDict.has_key(delete_name):
            showtable(delete_name)
            check = raw_input('确认删除？[y/n] ').strip()
            if check == 'y':
                del AddDict[delete_name]
                intofile(AddDict)
                print '删除成功！'
                break
            else:
                print '取消操作，请重新操作！'
                break
        else:
            print '没有查询到记录！'
def change():
    loadfile()
    while True:
        change_name = raw_input('输入要修改的姓名(q:返回) ').strip()
        if len(change_name) == 0: continue
        if change_name == 'q': break
        if AddDict.has_key(change_name):
            showtable(change_name)
            check = raw_input('是否要修改此条记录？[y/n] ').strip()
            if check == 'y':
                infoq = 0
                name = raw_input('姓名：').strip()
                ename = raw_input('英文名：').strip()
                department = raw_input('部门：').strip()
                tel = raw_input('分机号：').strip()
                mobile = raw_input('手机号：').strip()
                mail = raw_input('邮箱：').strip()
                if not AddDict.has_key(name):
                    del AddDict[change_name]
                AddDict[name] = [ename,department,tel,mobile,mail]
                showtable(name)
                check_change = raw_input('确认修改？[y/n] ').strip()
                if check_change == 'y':
                    intofile(AddDict)
                    print '修改成功！'
                    break
                else:
                    print '取消修改！'
                    break
        else:
                print '没有查询到记录！'
                continue

def query():
    loadfile()
    while True:
        global search
        search = raw_input('输入要查询的信息(q:返回)：').strip()
        if len(search) == 0: continue
        if search == "q": break
        if AddDict.has_key(search): 
            showtable(search)
        else:
            info_count = 0
            if len(search) < 3:
                print '请输入三个以上字符！'
                continue
            x = PrettyTable(["姓名","英文名","部门","分机号","手机号","邮箱"])
            x.align["姓名"] = "l"
            for name,value in AddDict.items():
                if name.count(search) != 0:
                    x.add_row([name,value[0],value[1],value[2],value[3],value[4]])
                    info_count += 1
                    continue
                for i in value:
                    if i.count(search) != 0:
                        x.add_row([name,value[0],value[1],value[2],value[3],value[4]])
                        info_count += 1
                        break
                if search == "***":
                    info_count += 1
                    x.add_row([name,value[0],value[1],value[2],value[3],value[4]])
            print x
            if info_count == 0:
                print '没有查询到记录！'
            else:
                print '找到%s条记录！' % info_count

while True:
    try:
        using()
        choice = raw_input("请选择：").strip()
        if len(choice) == 0:
            continue
        if choice == '1':
            add()
        elif choice == '2':
            delete()
        elif choice == '3':
            change()
        elif choice == '4':
            query()
        elif choice == '5':
            print 'Thank You, bye!'
            exit()
        else:
            print "\033[31;1m输入错误，请重新输入！\033[0m"
    except:
        print '\n程序退出...'
        sys.exit()



