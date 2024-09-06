import queue
class CustomQueue:

    def reverseQueue(self,q):
        if q.qsize() == 0:
            return
        front = q.get()
        self.reverseQueue(q)
        q.put(front)

q = queue.Queue()
q.put(1)
q.put(2)
q.put(3)
q.put(4)

# Reverse the queue
rq = CustomQueue()
rq.reverseQueue(q)

print("Reversed queue:")
while not q.empty():
    print(q.queue[0], end=" ")
    q.get()

    