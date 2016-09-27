import flask
from flask import Flask

# Create the application.
APP = Flask(__name__)

@APP.route('/')
def index():
    """ Displays the index page accessible at '/'
    """
    return flask.render_template('welcome.html')

@APP.route('/login-admin')
def index1 ():
    """ Displays the index page accessible at '/'
    """
    return flask.render_template('login_page_admin.html')

@APP.route('/login-student')
def loginStudent():
    """ Displays the index page accessible at '/'
    """
    return flask.render_template('index.html')




if __name__ == '__main__':
    APP.debug=True
    APP.run(host='0.0.0.0')
