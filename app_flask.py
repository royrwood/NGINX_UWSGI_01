from flask import Flask

application = Flask(__name__)

@application.route("/flask_app")
def hello():
    return "<h1 style='color:blue'>Hello There!</h1>"


if __name__ == "__main__":
    application.run(host='localhost')