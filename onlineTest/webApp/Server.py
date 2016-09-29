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



def checkStudent(email,password):
	print email
	sql1 = "SELECT * FROM STUDENT WHERE EMAIL = '%s'" % (email)
	try:
		cursor.execute(sq1l)
		results = cursor.fetchall()
		for row in results:
			fname= row[0]
			lname = row[1]
			demail = row[2]
			dpassword = row[3]
		print demail
		print dpassword
	except:
		print "Error: unable to fecth data"
	if( False):
		return True
	else:
		return False

@APP.route('/dashboard-student',methods = ['POST', 'GET'])
def studentDash():
	if request.method == 'POST':
		email=request.form['emailS']
		password=request.form['passwordS']
		if(checkStudent(email,password)):
			return render_template('dashboard_student.html')
		else:
			return render_template('login_page_student.html')




if __name__ == '__main__':
    APP.debug=True
    APP.run(host='0.0.0.0')
