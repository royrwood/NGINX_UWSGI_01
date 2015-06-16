# Note that this depends on Flask!
# I recommend that you create a Python virtual environment and then install Flask there, so something like this:
#  NGINX_UWSGI_01 roy$ virtualenv venv
#  NGINX_UWSGI_01 roy$ source venv/bin/activate
#  NGINX_UWSGI_01 roy$ pip install flask
#  NGINX_UWSGI_01 roy$ pip install uwsgi
#  NGINX_UWSGI_01 roy$ nginx -p . -c nginx.conf
#  NGINX_UWSGI_01 roy$ uwsgi --ini uwsgi.ini
#  NGINX_UWSGI_01 roy$ curl http://localhost:8000/flask/flask_app ; echo


from flask import Flask

application = Flask(__name__)

@application.route("/flask_app")
def hello():
    return "<h1 style='color:blue'>Hello There!</h1>"


if __name__ == "__main__":
    application.run(host='localhost')