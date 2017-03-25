#coding=utf-8
import pymysql.cursors


connect = pymysql.Connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='1234',
    db='boat',
    charset='utf8'
)


cursor = connect.cursor()


sql = "INSERT INTO gps (messageid, utc, state, latitude, ns, longitude, ew, speed, azimuth, date) VALUES ('%s', %f, '%s', %f, '%s', %f ,'%s', %f, %f, %d)"
data = ("$GPRMC",232133.42,"A",4234.43257,"N",12128.34123,"W",0.21,321.62,120599)
cursor.execute(sql % data)
connect.commit()
print('成功插入', cursor.rowcount, '条数据')


sql = "UPDATE gps SET speed = %.2f WHERE id = '%s' "
data = (0.58, '2')
cursor.execute(sql % data)
connect.commit()
print('成功修改', cursor.rowcount, '条数据')


sql = "SELECT id FROM gps WHERE speed > %f "
data = (0.20)
cursor.execute(sql % data)
#for row in cursor.fetchall():
#    print("Name:%s\tSaving:%.2f" % row)
print('共查找出', cursor.rowcount, '条数据')

#
#sql = "DELETE FROM gps WHERE account = '%s' LIMIT %d"
#data = ('13512345678', 1)
#cursor.execute(sql % data)
#connect.commit()
#print('�ɹ�ɾ��', cursor.rowcount, '������')


'''sql_1 = "UPDATE trade SET saving = saving + 1000 WHERE account = '18012345678' "
sql_2 = "UPDATE trade SET expend = expend + 1000 WHERE account = '18012345678' "
sql_3 = "UPDATE trade SET income = income + 2000 WHERE account = '18012345678' "

try:
    cursor.execute(sql_1)
    cursor.execute(sql_2)
    cursor.execute(sql_3)
except Exception as e:
    connect.rollback()
    print('������ʧ��', e)
else:
    connect.commit()  # �����ύ
    print('������ɹ�', cursor.rowcount)'''

# �ر�����
cursor.close()
connect.close()