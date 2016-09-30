import MySQLdb
db = MySQLdb.connect("localhost","root","pavilion@1","WEBAPP" )

cursor = db.cursor()

cursor.execute("DROP TABLE IF EXISTS STUDENT")

sql = """CREATE TABLE STUDENT (
         FIRST_NAME  CHAR(20) NOT NULL,
         LAST_NAME  CHAR(20)NOT NULL,
         EMAIL CHAR(20) NOT NULL,
         PASSWORD TEXT NOT NULL,
         PRIMARY KEY(EMAIL))"""

cursor.execute(sql)

cursor.execute("DROP TABLE IF EXISTS ADMIN")

sql = """CREATE TABLE ADMIN (
         FIRST_NAME  CHAR(20) NOT NULL,
         EMAIL CHAR(20) NOT NULL,  
         PASSWORD TEXT NOT NULL)"""

cursor.execute(sql)

cursor.execute("DROP TABLE IF EXISTS MARKS")

sql = """CREATE TABLE MARKS (
         FIRST_NAME  CHAR(20) NOT NULL,
         EMAIL CHAR(20) NOT NULL, 
         SCORE INT(20)NOT NULL,
         TEST_CODE TEXT NOT NULL,
         PRIMARY KEY(EMAIL))"""

cursor.execute(sql)


cursor.execute("DROP TABLE IF EXISTS TEST")

sql = """CREATE TABLE TEST (
         TEST_CODE TEXT NOT NULL,
         QUESTION  CHAR(100) NOT NULL,
         OPTION_A TEXT NOT NULL, 
         OPTION_B TEXT NOT NULL,
         OPTION_C TEXT NOT NULL,
         OPTION_D TEXT NOT NULL,
         ANSWER TEXT NOT NULL,
         PRIMARY KEY(QUESTION))"""

cursor.execute(sql)

db.close()