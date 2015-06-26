#!/usr/bin/env python
import MySQLdb
conn = MySQLdb.connect(host='10.10.1.1',user='root',passwd='*****',db='test',port=3306)
cursor = conn.cursor()
cursor.execute("show slave status")
rows = cursor.fetchall()
for row in rows:
    io = row[10]
    sql = row[11]
    if io == 'Yes' and sql == 'Yes':
        print "Mysql Slave is ok!"
    else:
        print "Mysql Slave is error!!!"
cursor.close()
conn.close()