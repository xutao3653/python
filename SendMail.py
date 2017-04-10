#!/usr/bin/env python
#_*_ coding:utf-8 _*_

import smtplib
from email.mime.text import MIMEText
mailto_list=['152XXXX1139@139.com']
mail_host="smtp.mxhichina.com"
mail_user="alert@XXXX.com"
mail_pass="123456"
mail_postfix="XXXX.com"

def send_mail(to_list,sub,content):
    me="hello"+"<"+mail_user+"@"+mail_postfix+">"
    msg = MIMEText(content,_subtype='plain',_charset='utf-8')
    msg['Subject'] = sub
    msg['From'] = me
    msg['To'] = ";".join(to_list)
    try:
        server = smtplib.SMTP()
        server.connect(mail_host)
        server.login(mail_user,mail_pass)
        server.sendmail(me, to_list, msg.as_string())
        server.close()
        return True
    except Exception, e:
        print str(e)
        return False
if __name__ == '__main__':
    if send_mail(mailto_list,"This is test mail.","hello world!"):
        print "发送成功"
    else:
        print "发送失败"
