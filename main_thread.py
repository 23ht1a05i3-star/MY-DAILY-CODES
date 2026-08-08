# '''
# what is program?
# A program is a se of instructions 
# stored on a disk

# print("hello")

# storing on a disk?

# what is process?
# when a program starts execution it becomes
# a process
# running?
# python hello.py
# hello

# OS --Operating system

# Chrome:
# Vs code:
# spotify:
# each one is a separate process

# characteristics:
# 1.Independent
# 2.Separate memory:
# Chrome:1.8GB, vs code:- 500MB
# 3.Heavy a weight:
# memory allocations
# resource allocations
# cpu scheduling

# what is a thread?
# A Thread is smallest unit of execution
# inside a process

# Restaurant == Process
# workers inside res = threads

# worker 1 - Taking the orders
# worker 2 - cooking
# worker 3 - 
# worker 4 - cleaning

# Visually:
# process:
# Chrome:
#    +thread1
#    +thread2
#    +thread3
 
# process                     |   thread
# 1.Independent               |  part of process
# 2.Heavy weight              |  Light weight
# 3.separate memory           |  Shared memory
# 4.Slow                      |  Fast
# 5.Expensive                 |  Cheap
# 6.Communication difficult   |  communication easy

# why threads are faster?
# threads will share the memory
# process needs separate memory allocation

# Concurrency?
# Teacher checking the notebooks
# student A
# student B
# student C

# Concurrency:
# A
# B
# C
# A
# B
# C
# one at a time
# rapidly switching
# appears simutaneously 
# CPU --ONLY ONE CPU

# Parallelism:
# cashier 1 --> customer 1
# cashier 2 --> customer 2
# cashier 3 --> customer 3
# truly simutaneous

# CPU1 --> Task a
# CPU2 --> Task b
# CPU3 --> Task c

# A
# B
# A
# B
# A
# B

# parallelism:
# cpu1 - AAA
# cpu2 - BBB

# one chef cooking:
# soup
# noodles
# fried rice

# parallelism:
# Chef 1 - soup
# Chef 2 - noodles
# Chef 3 - fried rice

# python threads will use ---concurrency
# due to GIL -Global interpreter lock

# '''
# #Creation of threads:
# import threading

# #Function Created (do's nothing)
# def display():
#     print("Hello")
# #Thread object (creation)
# t = threading.Thread(target=display)
# #start thread
# t.start()


# #multiple threads:
# import threading

# def task():
#     print("Thread running")
# t1 = threading.Thread(target=task)
# t2 = threading.Thread(target=task)
# t3 = threading.Thread(target=task)

# t1.start()
# t2.start()
# t3.start()

# '''
# Main Thread
#   + t1
#   + t2
#   + t3

#     all executes independently
# '''
# #Threads with loops

# def numbers():
#     for i in range(5):
#         print(i)
# t = threading.Thread(target=numbers)
# t.start()

# #Two threas with diff task
# def even():
#     for i in range(0,10,2):
#         print("Even:",i)

# def odd():
#     for i in range(1,10,2):
#         print("Odd:",i)

# t1 = threading.Thread(target=even)
# t2 = threading.Thread(target=odd)
# t1.start()
# t2.start()
#'''
#os scheduler decides:
#which thread to runs first?
import threading
print(threading.current_thread())

#Naming of Threads:
import threading

def task():
    print(threading.current_thread().name)

t = threading.Thread(target=task,
                     name="Student_Thread")
t.start()

#Passing arguments
def square(n):
    print(n*n)

t = threading.Thread(target=square,
                     args=(5,))
t.start()

#to delay threads
import time

print("start")
time.sleep(3)
print("end")

import threading
import time

def task():
    for i in range(5):
        print(i)
        time.sleep(1)

t = threading.Thread(target=task)
t.start()

# #retry mechanism
# while True:
#     try:
#         connect()
#     except:
#         time.sleep(5)

'''
join():mainthread -->owner
        worker thread --> worker





'''
import threading
import time
def task():
    time.sleep(3)
    print("Thread Finished")

t = threading.Thread(target=task)
t.start()
t.join()
print("Main thread ends here")

#Multiple threads with join
def task(name):
    print(name,"started")
    time.sleep(2)
    print(name,"Finished")

t1 =threading.Thread(
    target=task,args=("A",)
)
t2 =threading.Thread(
    target=task,args=("B",)
)
t1.start()
t2.start()

t1.join()
t2.join()

print("All threads completed")

#Example on naming threads
def task():
    print(threading.current_thread().name,
          "Started")
    time.sleep(2)

    print(threading.current_thread().name,
          "Finished")
t1 = threading.Thread(
    target=task, 
    name="download thread"
    )
t2 = threading.Thread(
    target=task, 
    name="upload thread"
    )
t1.start()
t2.start()