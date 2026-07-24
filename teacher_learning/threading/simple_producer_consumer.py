import queue
import threading
import time


message_queue = queue.Queue()


def producer():
    for number in range(5):
        print(f"Producing {number}")
        message_queue.put(number)
        time.sleep(0.5)


def consumer():
    for _ in range(5):
        item = message_queue.get()

        print(f"Processing {item}")
        time.sleep(1)


producer_thread = threading.Thread(target=producer)
consumer_thread = threading.Thread(target=consumer)

producer_thread.start()
consumer_thread.start()

producer_thread.join()
consumer_thread.join()

print("Finished")