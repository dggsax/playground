import threading
import queue
import requests

def test_worker():
    while True:
        try:
            print("LITLITLITLITLITLI")
        except Exception:
            print("death")
        else:
            print("I cry")

class StatusChecker(threading.Thread):
    """
    The thread that will check HTTP statuses.
    """

    #: The queue of urls
    url_queue = None

    #: The queue our results will go into
    result_queue = None

    #: Event thingy that tells threads to stop.
    stopper = None

    #: Target functions for use, optional
    target = None

    def __init__(self, url_queue, result_queue, stopper):
        super().__init__()
        self.url_queue = url_queue
        self.result_queue = result_queue
        self.stopper = stopper
        print(type(target))
        if type(target) != None:
            print(self.getName())

    def run(self):
        while True:
            try:
                # this will throw queue.Empty immediately if there's
                # no tasks left
                to_check = self.url_queue.get_nowait()
            except queue.Empty:
                break # empty queue, we're done
            else:
                resp = requests.get(to_check)
                self.result_queue.put((to_check, resp.status_code,))
                self.url_queue.task_done() # the the queue we're done

if __name__ == '__main__':
    url_queue = queue.Queue()
    result_queue = queue.Queue()


    for i in range(10):
        url_queue.put('http://jodalyst.com')
    stopper = threading.Event()
    num_workers = 4
    threads = list()

    for i in range(num_workers):
        t = StatusChecker(url_queue, result_queue, stopper)
        threads.append(t)
        print('Starting worker {}'.format(i))
        t.start()
        
    # wait for the queue to empty
    url_queue.join()

    while not result_queue.empty():
        url, status = result_queue.get_nowait()
        print('{} - {}'.format(url, status))