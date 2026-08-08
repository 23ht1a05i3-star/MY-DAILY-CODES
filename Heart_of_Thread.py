'''
1.Race Condition
2.Synchronization
3.Lock
4.RLock
'''
#why we need synchronization?

'''
balance = 1000

thread-1 --withdraw 500
thread-2 --withdraw 700

Both are accessing the same variables
without proper control

Incorrect Balance
wrong transactions
data corrupt

To avoid the above we will use:
Synchronization:
This is process of controlling access to shared
resources so that only one thread modifies at a time

Lock:
shared
resources: any variable,file,database,object

Example:

count = 0
if multiple threads modifies count simutaneously

#Race Condition:
occurs multiple threads access and modify
shared data simutaneously causing unpredictable
outputs


'''
count = 0
count +=1
print(count)

#Write with threads
import threading
count = 0                                       #count = variable
def increment():
    global count
    count +=1
    
threads = []
for i in range(1000):
    t = threading.Thread(target=increment)
    threads.append(t)
    t.start()
for t in threads:
    t.join()

print(count)
'''
998
994
998
'''
'''
critical section:
code section where shared resources are
accessed is called critical section
count +=1 --->critical section

To avoid the race condition?
one thread should enter critical section

solution: Lock

what is a lock?
synchronization Mechanism
that allows only one thread to execute
a critical section at a time.

Thread A acquries Lock
other Threads will wait
Thread A releases lock
next thread gets lock

import threading
lock = threading.Lock()

#to apply lock
lock.acquire()

#to release
lock.release()

'''
