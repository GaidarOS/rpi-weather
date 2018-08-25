# -*- coding: utf-8 -*-
from random import randrange, uniform
from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from time import sleep
# from RPi import read_temp

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

def sensor_read():
    with open("hello.txt", "w") as f:
        data = randrange(10, 25) * uniform(0.8, 1)
        f.write(str(data))

    with open("hello.txt", "r") as f:
        data = f.read()

    return data


@app.route('/')
def index():
    return render_template('index.html')


@socketio.on('client_connected')
def handle_client_connect_event(json):
    print('received json: {0}'.format(str(json)))


@socketio.on('json')
def handle_json_button():
    # it will forward the json to all clients.
    # print("This it the json message: ", json)
    # sleep(2)
    emit('json', sensor_read())
    # Comment line above and uncomment the ones below to send the values from the temp sensor
    # c,f = read_temp()
    # emit('json', c)


# @socketio.on('alert_button')
# def handle_alert_event(json):
#     # it will forward the json to all clients.
#     print('Message from client was {0}'.format(json))
#     emit('alert', sensor_read())


if __name__ == '__main__':
    # socketio.run(app, host="0.0.0.0", port=27346, debug=True)
    socketio.run(app, host="0.0.0.0", port=27346)
