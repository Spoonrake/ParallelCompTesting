import threading
import time
import os

os.system("cls")
def writer():
    while True:
        print(round(time.time()))
        time.sleep(1)
        os.system("cls")

writer()

"""
# init threads
t1 = threading.Thread(target=writer, args=(0, e1, e2))
t2 = threading.Thread(target=writer, args=(1, e2, e1))

# start threads
t1.start()
t2.start()

e1.set() # initiate the first event

# join threads to the main thread
t1.join()
t2.join()
"""
