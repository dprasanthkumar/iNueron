import mysql.connector
# import mysql.connector
#create user 'user'@'%' identified by 'password'
mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)
print(mydb.is_connected())

#***********************************************************************************************

cur=mydb.cursor()
cur.execute('show databases')
for a in cur:
    print(a)

cur.execute("select * from sample.students")
for b in cur:
    print(b)
import mysql.connector
# import mysql.connector
#create user 'user'@'%' identified by 'password'
mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)

cur=mydb.cursor()
#cur.execute("create database two")

#cur.execute('create table two.one(Prasanth varchar(20),Pradeep varchar(20),Prathibha varchar(20))')

mydb.commit()
