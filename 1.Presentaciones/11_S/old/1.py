import Queue
import threading
import urllib2
import time

# called by each thread
def get_url(q, url):
    time.sleep(10)
    q.put(urllib2.urlopen(url).read())


theurls = ["http://eltiempo.com", "http://elcolombiano.com", "http://elmundo.com", "http://elpais.com"]

q = Queue.Queue()

for u in theurls:
    t = threading.Thread(target=get_url, args = (q,u))
    t.daemon = True
    t.start()

s = q.get()
print s
