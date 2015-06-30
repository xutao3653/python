# python常用脚本

###tab.py
用于python补全

###backup_file.py
用来备份目录或文件，修改其中的Source_Path源目录、Target_Dir目标目录即可。

###check_mysql_slave.py
用来监控mysql的主从复制状态是否正常

###prettytable.py
用来表格显示，更加美观

用法：

from prettytable import PrettyTable

a = PrettyTable(["姓名","英文名","部门","分机号","手机号","邮箱"])

a.align["姓名"] = "l"

a.add_row([name, AddDict[name][0], AddDict[name][1], AddDict[name][2], AddDict[name][3], AddDict[name][4] ])

print a

###AddressBook.py
学习脚本，通讯簿小程序

###SendMail.py
邮件发送

用法：

from SendMail import send_mail

send_mail('mail_to','sub','message')
