import pyaudio

p = pyaudio.PyAudio()

# For figuring out damn host stuff lmao
print(p.get_host_api_count())
print(p.get_default_input_device_info())

# Select Device
device = p.get_device_info_by_host_api_device_index(0L, 2L)

# # Device Specs
# CHUNK = 2048 # how big the fft array will be
# CHANNELS = int(device['maxInputChannels'])
# FORMAT = pyaudio.paFloat32
# RATE = int(device['defaultSampleRate'])
# START = 0
# N = CHUNK  

# stream = pa.open(
#     format = FORMAT,
#     channels = CHANNELS, 
#     rate = RATE,
#     input = True,
#     output = False,
#     input_device_index = 2L,
#     frames_per_buffer = CHUNK)