# For stack we can use list but for queue we can not use list as for dequeue it takes O(n) operations

import queue

q = queue.Queue()
q.put(1)
q.put(2)
q.put(3)
q.put(4)
q.put(5)
while not q.empty():
    print(q.get())

print('Stack')

s = queue.LifoQueue()
s.put(1)
s.put(2)
s.put(3)
s.put(4)

while not s.empty():
    print(s.get())
