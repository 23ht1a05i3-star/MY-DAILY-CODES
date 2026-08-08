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
