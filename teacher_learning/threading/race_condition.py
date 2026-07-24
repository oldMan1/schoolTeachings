import threading
import time

counter = 0


def increase_counter(name):
    global counter

    old_value = counter

    print(f"{name} read: {old_value}")

    time.sleep(1)

    counter = old_value + 1

    print(f"{name} wrote: {counter}")


thread_1 = threading.Thread(
    target=increase_counter,
    args=("Thread A",)
)

thread_2 = threading.Thread(
    target=increase_counter,
    args=("Thread B",)
)

thread_1.start()
thread_2.start()

thread_1.join()
thread_2.join()

print("Final counter:", counter)