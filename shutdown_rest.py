import pystray
from PIL import Image, ImageDraw
from pystray import Menu, MenuItem
from flask import Flask
import threading
import signal
import os
import subprocess


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/shutdown')
def shutdown():
    subprocess.call('shutdown -s -t 60', shell=True)
    return 'Shutting Down'


@app.route('/cancel_shutdown')
def cancel_shutdown():
    subprocess.call('shutdown -a', shell=True)
    return 'Canceling shutdown'


def exit_action(icon):
    print('start killing app')
    icon.visible = False
    icon.stop()
    print('Killed icon')
    print('killing pid:', os.getpid())
    os.kill(os.getpid(), signal.SIGTERM)
    print('Killed flask')


def init_icon(color=(255, 0, 0)):

    icon = pystray.Icon('mon')
    icon.menu = Menu(
        MenuItem('Shutdown', lambda: shutdown()),
        MenuItem('Cancel Shutdown', lambda: cancel_shutdown()),
        MenuItem('Exit', lambda: exit_action(icon))
    )
    if os.path.exists('shutdown.png'):
        img = Image.open('shutdown.png')
    else:
        img = Image.new('RGBA', (128, 128), (0, 0, 0, 0))
        draw = ImageDraw.Draw(img)
        draw.arc((5 + 10, 5 + 20, 125 - 10, 125),
                 start=295, end=245, fill=color, width=13)
        draw.line(((64, 10), (64, 70)), fill=color, width=13)
    icon.icon = img
    icon.title = 'Shutdown REST'

    icon.run()


def init_flask():
    app.run(host='0.0.0.0', port=5000)


threading.Thread(target=init_flask).start()
init_icon()
