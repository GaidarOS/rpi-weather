# -*- coding: utf-8 -*-
# Start with a basic flask app webpage.
from random import random, randrange, uniform
from flask import Flask, render_template, url_for, copy_current_request_context
from flask_socketio import SocketIO, emit
from time import sleep
from threading import Thread, Event
# from RPi import read_temp


__author__ = 'VK'

#random number Generator Thread
thread = Thread()
thread_stop_event = Event()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


class RandomThread(Thread):
    def __init__(self, delay=1):
        self.delay = delay
        super(RandomThread, self).__init__()

    def randomNumberGenerator(self):
        """
        Generate a random number every 1 second and emit to a socketio instance (broadcast)
        Ideally to be run in a separate thread?
        """
        #infinite loop of magical random numbers
        print("Making random numbers")
        while not thread_stop_event.isSet():
            number = round(randrange(10, 25) * uniform(0.8, 1), 3)
            # print(number)
            socketio.emit('newnumber', {'number': number}, namespace='/temperature')
            sleep(self.delay)

    def run(self):
        self.randomNumberGenerator()


@app.route('/')
def index():
    return render_template('index.html')


@socketio.on('connect', namespace='/temperature')
def test_connect():
    # need visibility of the global thread object
    global thread
    print('Client connected')

    #Start the random number generator thread only if the thread has not been started before.
    if not thread.isAlive():
        print("Starting Thread")
        thread = RandomThread(delay=3)
        thread.start()

@socketio.on('disconnect', namespace='/temperature')
def test_disconnect():
    print('Client disconnected')

if __name__ == '__main__':
    # socketio.run(app, host="0.0.0.0", port=27346, debug=True)
    socketio.run(app, host="0.0.0.0", port=27346)
