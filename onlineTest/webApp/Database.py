import MySQLdb
db = MySQLdb.connect("localhost","root","pavilion@1","WEBAPP" )

cursor = db.cursor()

cursor.execute("DROP TABLE IF EXISTS STUDENT")

sql = """CREATE TABLE STUDENT (
         FIRST_NAME  CHAR(20) NOT NULL,
         LAST_NAME  CHAR(20)NOT NULL,
         EMAIL CHAR(20) NOT NULL,
         PASSWORD CHAR(20)NOT NULL,
         PRIMARY KEY(EMAIL))"""

cursor.execute(sql)

cursor.execute("DROP TABLE IF EXISTS ADMIN")

sql1 = """CREATE TABLE ADMIN (
         FIRST_NAME  CHAR(20) NOT NULL,
         EMAIL CHAR(20) NOT NULL,  
         PASSWORD CHAR(20)NOT NULL)"""

cursor.execute(sql1)

cursor.execute("DROP TABLE IF EXISTS MARKS")

sql2 = """CREATE TABLE MARKS (
         FIRST_NAME  CHAR(20) NOT NULL,
         EMAIL CHAR(20) NOT NULL, 
         SCORE CHAR(20)NOT NULL,
         PRIMARY KEY(EMAIL))"""

cursor.execute(sql2)
db.close()