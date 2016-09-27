import flask


# Create the application.
APP = flask.Flask(__name__)


@APP.route('/')
def index():
    """ Displays the index page accessible at '/'
    """
    return flask.render_template('login_page_student.html')


if __name__ == '__main__':
    APP.debug=True
    APP.run(host='0.0.0.0')