import time
import math
import numpy as np
import pyaudio
import sys

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

    # Initializes whenever the class object is called.
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
        # lines 69 and 70 chop the array in half, and then flip it
        # and voila we're returning an fft!
        half_y = len((self.spec_y))/2
        half_x = len((self.spec_x))/2
        self.spec_y = self.spec_y[:half_y]
        self.spec_x = self.spec_x[:half_x]
        # return self.spec_x[::-1], self.spec_y[::-1]
        return self.spec_x, self.spec_y

# First time setup
first_time = True
if ( first_time ):
    # Initialize a class object
    wow = SpectrumAnalyzer()
    first_time = False

try:
    while True:
        print("hi")
        print(wow.fft())
        time.sleep(.02)    # can't sleep for any faster than .02.
except IOError:
    print("IO Error. Probably input overflowed.")
    print("Make sure that as you loop through")
    print("the fft() function of the Spectrum")
    print("class that you give it enough time")
    print("to sleep. I found that it has to be")
    print("less than .02 seconds. It's annoying,")
    print(" I know. Errno -9981 in case you ")
    print("were wondering.")
