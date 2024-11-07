from flask import Flask

application = Flask(__name__)  # Elastic Beanstalk looks for application by default.

@application.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    application.run(debug=True, host='0.0.0.0')
