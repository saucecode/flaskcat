# flaskcat

A chat server written in python 2.7, using flask and websockets.

____

Requires:

    pip install flask
    pip install Flask-Sockets

Also requires *gunicorn* to run, in order to add WebSocket functionality into the flask server. More information about this can be read about on the [Flask-Sockets repo](https://github.com/kennethreitz/flask-sockets).

Run with ./start.sh. Or alternatively,

    gunicorn -k flask_sockets.worker -b localhost:1234 flaskchat:app

Change the bind address as needed.

____

The "h" in *flaskcat* was deliberately dropped for you, because cats are cool, and you are too.   Rest in peace, kadence.
