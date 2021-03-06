import time
import math
from threading import Thread, Lock
from flask import Flask, render_template, session, request
from flask_socketio import SocketIO, emit, join_room, leave_room,close_room, rooms, disconnect
import pyaudio
import numpy as np
# Set this variable to "threading", "eventlet" or "gevent" to test the
# different async modes, or leave it set to None for the application to choose
# the best option based on available packages.
#async_mode = 'threading'
#async_mode = 'eventlet'
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

def micThread():
    # First time setup
    first_time = True
    if ( first_time ):
        wow = SpectrumAnalyzer()
        first_time = False

    # Etc
    # There's a bunch of timing stuff in here that really isn't
    # necessary for you to understand, but like like 90 is pretty
    # as you can see it will send the update_457 socket that 
    # the microphone.html will listen for
    unique = 456
    burst_duration = 1
    counter = 0
    toggle_count = 500
    on_state = True
    while True:
        counter +=1
        if counter%burst_duration == 0:
            socketio.emit('update_{}'.format(unique+1),wow.fft(),broadcast =True)
        if counter%toggle_count == 0:
            counter = 0
            if on_state:
                print("OFF")
            else:
                print("ON")
            on_state = not on_state
        
        time.sleep(0.001)


class SpectrumAnalyzer:
    # Start Pyaudio
    p = pyaudio.PyAudio()

    # Select Device
    device = p.get_device_info_by_host_api_device_index(0, 0)

    # Device Specs
    CHUNK = 2048 # how big the fft array will be
    CHANNELS = int(device['maxInputChannels'])
    FORMAT = pyaudio.paFloat32
    RATE = int(device['defaultSampleRate'])
    START = 0
    N = CHUNK  

    # Setting up stuffs
    wave_x = 0
    wave_y = 0
    spec_x = 0
    spec_y = 0
    data = []

    def __init__(self):
        # This sets up the audio stream where we start a stream
        # that inputs a live audio feed.
        # When joe sends you his microphone, we'll need to modify
        # the value of input_device_index. Let me know when he 
        # sends it to you!
        self.pa = pyaudio.PyAudio()
        self.stream = self.pa.open(
            format = self.FORMAT,
            channels = self.CHANNELS, 
            rate = self.RATE,
            input = True,
            output = False,
            input_device_index = 0,
            frames_per_buffer = self.CHUNK)

    # This inputs audio from the stream and then returns data in an array
    # Note the np.flaot32, we are dealing with 32 byte floats! So, numbers
    # that are either really big or really small with lots of decimals
    def audioinput(self):
        data = np.fromstring(self.stream.read(self.CHUNK),dtype=np.float32)
        return data

    # This takes the data stream and performs the fft.
    def fft(self):
        self.data = self.audioinput()
        # Unsure what wave_x and wave_y do at the moment, 
        # need to figure that out in a bit
        self.wave_x = range(self.START, self.START + self.N)
        self.wave_y = self.data[self.START:self.START + self.N]
        # This is the important stuff. This generates the x and y values
        self.spec_x = np.fft.fftfreq(self.N, d = 1.0 / self.RATE) 
        y = np.fft.fft(self.data[self.START:self.START + self.N])
        # This is where the fourier transform math happens. Um, as I 
        # said in my initial email to you, it's hard stuff.
        self.spec_y = [np.sqrt(c.real ** 2 + c.imag ** 2) for c in y]
        # The fft array that line 161 returns is mirrored so essentially
        # lines 163 and 164 chop the array in half, and then flip it
        # and voula we're returning an fft!
        half = len((self.spec_y))/2
        self.spec_y = self.spec_y[:half]
        return self.spec_y[::-1]

# Start the web app
@app.route('/')
def index():
    global thread
    print ("A user connected")
    if thread is None:
        # Start the micThread (the live fft stuffs)
        thread = Thread(target=micThread)
        thread.daemon = True
        thread.start()
    # Build the website!
    return render_template('microphone.html')


if __name__ == '__main__':
    socketio.run(app, port=3000, debug=True)