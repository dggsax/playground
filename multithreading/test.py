##################################################################################
##                                                                              ##
##    Beginning of code to handle multiple threads, let's see how it goes...    ##
##                                                                              ##         
##################################################################################

import logging
import threading
import time

# Set up a logger
logging.basicConfig(level=logging.DEBUG,
                    format='[%(levelname)s] (%(threadName) - 10s) %(message)s'
                    )

def worker():
    while True:
        logging.debug("hi")
    # try:
    #     logging.debug("Hello!")
    # except Exception:
    #     logging.debug("death :(")

class threadManager(threading.Thread):

    # Initialize
    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs=None, verbose=None):
        threading.Thread.__init__(self, group=group, target=target, name=name,
                                  verbose=verbose) 
        self.name = name
        self.target = target
        self.args = args
        self.kwargs = kwargs
        return

    def run(self):
        logging.debug('Starting with args: %s and kwargs: %s',self.args,self.kwargs)
        return
    def demon(self):
        self.setDaemon(True)
        return
# Yeshua = threadManager( name='Yeshua' , daemon=True)
# Yeshua = threadManager( name='Yeshua' )
# Yeshua = threadManager( name='Yeshua' , target=worker())
# Gonzo = threadManager( name='Gonzo' , target=worker())
# Yeshua = threadManager( name='Yeshua' , target=worker() , daemon=True)
# Yeshua.start()
# Gonzo.start()
# Yeshua.test()
# print(Yeshua)
# time.sleep(5)
# print(Yeshua)
# print(Gonzo)

for i in range(5):
    # t = threadManager(args=(i,))
    t = threadManager(name="Joe"+str(i), target=worker)
    # t.demon()
    t.start()
