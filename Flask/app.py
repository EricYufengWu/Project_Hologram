from flask import Flask, render_template, Response
from flask_socketio import SocketIO
import cv2
import threading
import requests
import time

app = Flask(__name__)
socketio = SocketIO(app)

# Store the image URL as a global variable
image_url = 'images/tennis01.jpg'

@app.route('/left')
def left():
    global image_url
    image_url = 'images/tennis02.jpg'
    return "Image updated"


@app.route('/right')
def right():
    global image_url
    image_url = 'images/tennis03.jpg'
    return "Image updated"


@app.route('/default')
def default():
    global image_url
    image_url = 'images/tennis01.jpg'
    return "Image updated"


@app.route('/')
def index():
    return render_template('index.html', image_url=image_url)


if __name__ == '__main__':
    app.run()

'''
Run Instructions
Navigate to the project folder in a terminal and run "flask run"
'''
