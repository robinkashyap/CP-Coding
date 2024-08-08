
def printKFreqWord(s, k):
    words = s.split()
    d = {}
    for i in words:
        d[i] = d.get(i,0) + 1
    for j in d:
        if d[j] == 2:
            print(j) 

s = 'This is a word string having many many word'
result = printKFreqWord(s,2)
