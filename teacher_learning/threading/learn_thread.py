import threading 
import time

def task1():
    print("Task 1 started")
    time.sleep(5)
    print("Task 1 completed")

def task2():
    print("Task 2 started")
    time.sleep(15)
    print("Task 2 completed")

def task3():
    print("Task 3 started")
    time.sleep(10)
    print("Task 3 completed")

if __name__ == "__main__":
    thread1 = threading.Thread(target=task1)
    thread2 = threading.Thread(target=task2)
    thread3 = threading.Thread(target=task3)

    thread1.start()
    thread2.start()
    thread3.start()

    thread1.join()
    thread2.join()
    thread3.join()

    print("All tasks completed")