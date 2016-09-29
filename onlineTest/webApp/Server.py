import flask
from flask import Flask, request, render_template

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



    
@APP.route('/dashboard-admin',methods = ['POST', 'GET'])
def adminDash():
	if request.method == 'POST':
		name=request.form['name']
		email=request.form['email']
    	return render_template('dashboard_admin.html', name=name, email=email)




@APP.route('/dashboard-student')
def studentDash():
    return render_template('dashboard_student.html')




if __name__ == '__main__':
    APP.debug=True
    APP.run(host='0.0.0.0')
