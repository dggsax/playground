from flask import Flask, render_template, session, request, make_response
from flask_socketio import SocketIO, emit, join_room, leave_room,close_room, rooms, disconnect
import glob
import json
import math
from threading import Thread, Lock
import time
import serial
import sys
import struct

import logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

async_mode = None
if async_mode is None:
    try:
        import eventlet
        async_mode = 'eventlet'
    except ImportError:
        pass

    if async_mode is None:
        try:
            from gevent import monkey
            async_mode = 'gevent'
        except ImportError:
            pass

    if async_mode is None:
        async_mode = 'threading'

    print('async_mode is ' + async_mode)

# monkey patching is necessary because this application uses a background
# thread
if async_mode == 'eventlet':
    import eventlet
    eventlet.monkey_patch()
elif async_mode == 'gevent':
    from gevent import monkey
    monkey.patch_all()

#Start up Flask server:
app = Flask(__name__, template_folder = './',static_url_path='/static')
app.config['SECRET_KEY'] = 'secret!' #shhh don't tell anyone. Is a secret
socketio = SocketIO(app, async_mode = async_mode)
thread = None

def dataThread():
    pass

# Startup has occured
@app.route('/')
def index():
    global thread
    print ("A user connected")
    if thread is None:
        thread = Thread(target=dataThread)
        thread.daemon = True
        thread.start()
    return render_template('liveplot.html')

@app.route("/simple.png")
def simple():
    import datetime
    import io
    import random

    from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
    from matplotlib.figure import Figure
    from matplotlib.dates import DateFormatter

    try:
        while True:
            fig=Figure()
            ax=fig.add_subplot(111)
            x=[]
            y=[]
            now=datetime.datetime.now()
            delta=datetime.timedelta(days=1)
            for i in range(10):
                x.append(now)
                now+=delta
                y.append(random.randint(0, 1000))
            ax.plot_date(x, y, '-')
            ax.xaxis.set_major_formatter(DateFormatter('%Y-%m-%d'))
            fig.autofmt_xdate()
            canvas=FigureCanvas(fig)
            png_output = io.BytesIO()
            canvas.print_png(png_output)
            response=make_response(png_output.getvalue())
            response.headers['Content-Type'] = 'image/png'
            return response
            time.sleep(.001)
            fig.cla()
    except:
        print('welp')


if __name__ == '__main__':
    socketio.run(app, port=3000, debug=True)




















