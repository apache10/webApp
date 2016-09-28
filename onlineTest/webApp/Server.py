import flask
from flask import Flask, request, render_template

# Create the application.
APP = Flask(__name__)

@APP.route('/')
def welcome ():
    """ Displays the index page accessible at '/'
    """
    return flask.render_template('welcome.html')

@APP.route('/login-admin')
def loginAdmin ():
 
    return render_template('login_page_admin.html')

@APP.route('/login-student')
def loginStudent():

    return render_template('login_page_student.html')
    
@APP.route('/dashboard-admin')
def adminDash():
    return render_template('dashboard_admin.html')

@APP.route('/dashboard-student')
def studentDash():
    return render_template('dashboard_student.html')




if __name__ == '__main__':
    APP.debug=True
    APP.run(host='0.0.0.0')
