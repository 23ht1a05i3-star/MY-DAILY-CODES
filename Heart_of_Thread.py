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
import threading
count = 0
lock = threading.Lock()

def increment():
    global count
    for i in range(10000):
        with lock:
        #critical section
            count +=1
        
t1 = threading.Thread(target=increment)
t2 = threading.Thread(target=increment)

t1.start()
t2.start()

t1.join()
t2.join()

print(count)

#Bank example:
class Bank:
    def __init__(self):
        self.balance = 1000

    def withdraw(self,amount):
        if self.balance >= amount:
            self.balance -= amount

#T1 = 500
#T2 = 700          #negative

import threading
class Bank:
    def __init__(self):
        self.balance  = 1000
        self.lock = threading.Lock()
    def withdraw(self,amount):
        with lock:
            if self.balance >= amount:
                self.balance -= amount
                print(amount,"withdraw")
            else:
                print("Insufficient Balance")
bank = Bank()
t1 = threading.Thread(
    target=bank.withdraw,
    args= (700,)
)
t2 = threading.Thread(
    target=bank.withdraw,
    args= (500,)
)
t1.start()
t2.start()

t1.join()
t2.join()
print(bank.balance)

'''
Deadlock:
Where the threds wait forever for locks
Thread 1
Lock A
waiting for Lock B

Thread 2
Lock B
waiting for Lock A

Thread 1 --> Lock A
Thread 2 --> Lock B
deadlock


Rlock:
a thread can acquire same lock multiple times

whyRlock/;
normal lock
acquire lock
release lock

if same lock acquire again dead lock
'''
# import threading
# lock=threading.Lock()
# def outer():
#     lock.acquire()
#     inner()
#     lock.release()
# def inner():
#     lock.acquire()
#     print("inner")
#     lock.release()
# outer()
'''
outre() acquire the lock
inner() trying to acquire the same lock
lock is already head above
wait forever
'''
lock=threading.RLock()
def inner():
    with lock:
        print("inner")
def outer(): 
    with lock:
        print("outer")
        inner()
outer()
'''
outer acquire
count = 1

inner acquire
count=2
inner releases the lock
count = 1
outer  release the lock
count = 2
'''


#Real world teacher problem and time 
import threading
import time

def student(name):
    print(name,"started exam")
    time.sleep(3)
    print(name,"Submitted paper")

t1 = threading.Thread(target=student,
                      args=("Ranjith",),
                      name="Student-1"
)
t2 = threading.Thread(target=student,
                      args=("Anand",),
                      name="student-2"
)
t1.start()
t2.start()
t1.join()
t2.join()
print("Teacher collected all papers")