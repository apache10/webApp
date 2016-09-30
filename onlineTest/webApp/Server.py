import flask
from flask import Flask, request, render_template
import MySQLdb
db = MySQLdb.connect("localhost","root","pavilion@1","WEBAPP" )
cursor = db.cursor()

# Create the application.
APP = Flask(__name__)



@APP.route('/')
def welcome ():
    return flask.render_template('welcome.html')



@APP.route('/login-admin')
def loginAdmin ():
    return render_template('login_page_admin.html')



@APP.route('/login-student')
def loginStudent():
    return render_template('login_page_student.html')



@APP.route('/registred',methods = ['POST', 'GET'])
def registred():
	if request.method == 'POST':
		fname=request.form['name']
		lname=request.form['last']
		email=request.form['email']
		password=request.form['password']
		if(checkRegister(fname,lname,email,password)):
			return render_template('registered.html')
		else:
			return render_template('unsucessful.html')

@APP.route('/upload-Question',methods =['POST', 'GET'])
def uploadQuestion():
	if request.method == 'POST':
		testCode=request.form['testCode']
		question=request.form['question']
		optionA=request.form['optionA']
		optionB=request.form['optionB']
		optionC=request.form['optionC']
		optionD=request.form['optionD']
		answer=request.form['answer']
		if(checkUpload(testCode,question,optionA,optionB,optionC,optionD,answer)):
			return render_template('dashboard_admin.html')
		else:
			return render_template('dashboard_admin.html')
    
@APP.route('/dashboard-admin',methods = ['POST', 'GET'])
def adminDash():
	if request.method == 'POST':
		name=request.form['name']
		email=request.form['email']
		password=request.form['password']
		if(checkAdmin(name,email,password)):
			return render_template('dashboard_admin.html', name=name, email=email)
		else:
			return render_template('login_page_admin.html')


@APP.route('/dashboard-student',methods = ['POST', 'GET'])
def studentDash():
	if request.method == 'POST':
		email=request.form['emailS']
		password=request.form['passwordS']
		if(checkStudent(email,password)):
			return render_template('dashboard_student.html',email=email)
		else:
			return render_template('login_page_student.html')



def checkUpload(testCode,question,optionA,optionB,optionC,optionD,answer):
	check=False
	sql= "INSERT INTO TEST(TEST_CODE, QUESTION, OPTION_A, OPTION_B, OPTION_C, OPTION_D, ANSWER) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s')" %(testCode,question,optionA,optionB,optionC,optionD,answer)
	try:
		cursor.execute(sql)
		db.commit()
		check=True
	except:
		db.rollback()

	if(check):
		return True
	else:
		return False


def checkAdmin(name,email,password):
	sql = "SELECT * FROM ADMIN WHERE EMAIL = '%s'" % (email)
	try:
		cursor.execute(sql)
		results = cursor.fetchall()
		for row in results:
			fname = row[0]
			demail = row[1]
			dpassword = row[2]
	except:
		print "Error: unable to fecth data"
	if( dpassword == password):
		return True
	else:
		return False



def checkStudent(email,password):
	sql = "SELECT * FROM STUDENT WHERE EMAIL = '%s'" % (email)
	try:
		cursor.execute(sql)
		results = cursor.fetchall()
		for row in results:
			fname= row[0]
			lname = row[1]
			demail = row[2]
			dpassword = row[3]
	except:
		print "Error: unable to fecth data"
	if(password==dpassword):
		return True
	else:
		return False


def checkRegister(fname,lname,email,password):
	count=False
	sql= "INSERT INTO STUDENT(FIRST_NAME,LAST_NAME, EMAIL, PASSWORD) VALUES ('%s', '%s', '%s', '%s')" 	%(fname,lname,email,password)
	try:
		cursor.execute(sql)
		db.commit()
		count=True
	except:
		db.rollback()

	if(count):
		return True
	else:
		return False


if __name__ == '__main__':
    APP.debug=True
    APP.run(host='0.0.0.0')