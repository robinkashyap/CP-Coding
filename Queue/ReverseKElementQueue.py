import queue
class Reverse:
    def reverse(self,q,k):
        if q.qsize()==0:
            return
        li = []
        for i in range(k):
            li.append(q.get())
        while li:
            q.put(li.pop())
        for i in range(q.qsize()-k):
            q.put(q.get())
        

st = queue.Queue()
st.put(1)
st.put(2)
st.put(3)
st.put(4)
st.put(5)
k = 3
qu = Reverse()
qu.reverse(st,k)

while not st.empty():
    print(st.get(), end=" ")