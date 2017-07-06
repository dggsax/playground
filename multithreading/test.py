##################################################################################
##                                                                              ##
##    Beginning of code to handle multiple threads, let's see how it goes...    ##
##                                                                              ##         
##################################################################################

import logging
import threading
import time

# Set up a logger
logging.basicConfig(level=logging.DEBUG, # The level that we want it to Debug.
                    format='[%(levelname)s] (%(threadName) - 10s) %(message)s')




def worker():
    # This is really cool, general for all threads!
    logging.debug('Starting')
    time.sleep(2)
    # Same here!
    logging.debug('Exiting')

def my_service():
    logging.debug('Starting')
    time.sleep(2)
    logging.debug('Exiting')


def main():
    t = threading.Thread(name='my_service', target=my_service)
    w = threading.Thread(name='worker', target=worker)
    w2 = threading.Thread(target=worker)

    t.start()
    w.start()
    w2.start()

# class threadmanager(name, worker_function):
#     def __init__(self,name,worker_function):
#         # (Hopefully) make the thread
#         self.name = self.threading.Thread(name=Str(name), worker=worker_function)
        
#         # Instantiate a loop to do shit
#         self.loop()

#     def loop(self):
#         try:
#             while True:
#                 print(threading.currentThread().getName(), 'Yoooo')
#                 time.sleep(3)
#                 print(threading.currentThread().getName(), 'I"m back thot')
#                 time.sleep(3)
#         except:
#             print("Damn :(")

if __name__ == '__main__':
    main()



'''
class SpectrumAnalyzer:

    def __init__(self):
        self.pa = pyaudio.PyAudio()
        self.stream = self.pa.open(
            format = self.FORMAT,
            channels = self.CHANNELS, 
            rate = self.RATE,
            input = True,
            output = False,
            input_device_index = 0,
            frames_per_buffer = self.CHUNK)
    #     #Main Loop
    #     self.loop()
'''