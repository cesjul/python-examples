from threading import Thread
from time import sleep

class MyThread(Thread):
    def __init__(self, text, time):
        self.text = text
        self.time = time
        super().__init__()

    def run(self):
        sleep(self.time)
        print(self.text)
    
t1 = MyThread('Thread', 10)
t1.start()

t2 = MyThread('Thread 1', 2)
t2.start()

t3 = MyThread('Thread 2', 1)
t3.start()

# while t1.is_alive():
    
#     print('thread 1 is running')
