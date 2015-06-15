# NGINX_UWSGI_01
Just some messing around with NGINX and UWSGI.

So far, there is a trivial Flask app, and things are set up so that the Flask app is served up by UWSGI, 
which is in-turn fronted by NGINX.


To run things, start up UWSGI, then start up NGINX, so do something like the following.  
Note that the NGINX [alert] can be ignored (it tries to do some logging before switching to the specified config,
and the default log location, /var/log/nginx/error.log, is not writable by non-root accounts).
And yes, in the following examples, I am running in a Python virtual env, "venv".  

(venv)rrwood@ubuntu-HP-DV2000:~/Python$ ls -l
total 4
drwxrwxr-x 6 rrwood rrwood 4096 Jun 14 20:21 flask_01

(venv)rrwood@ubuntu-HP-DV2000:~/Python$ cd flask_01/

(venv)rrwood@ubuntu-HP-DV2000:~/Python/flask_01$ uwsgi --ini uwsgi.ini                                                                
[uWSGI] getting INI configuration from uwsgi.ini

(venv)rrwood@ubuntu-HP-DV2000:~/Python/flask_01$ nginx -p . -c nginx.conf
nginx: [alert] could not open error log file: open() "/var/log/nginx/error.log" failed (13: Permission denied)

(venv)rrwood@ubuntu-HP-DV2000:~/Python/flask_01$ ps -e | grep uwsgi
31008 ?        00:00:00 uwsgi
31011 ?        00:00:00 uwsgi
31012 ?        00:00:00 uwsgi
(venv)rrwood@ubuntu-HP-DV2000:~/Python/flask_01$ ps -e | grep nginx
31016 ?        00:00:00 nginx
31017 ?        00:00:00 nginx

(venv)rrwood@ubuntu-HP-DV2000:~/Python/flask_01$ curl http://localhost:8000/static/test.txt ; echo
This is test.txt.

(venv)rrwood@ubuntu-HP-DV2000:~/Python/flask_01$ curl http://localhost:8000/flask/flask_app ; echo
<h1 style='color:blue'>Hello There!</h1>


