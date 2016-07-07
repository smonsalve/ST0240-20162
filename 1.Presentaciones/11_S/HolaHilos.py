import threading
import datetime

class ThreadClass(threading.Thread):
  def run(self):
    now = datetime.datetime.now()
    print "soy el hilo %s, hola a las: %s" % (self.getName(), now)

for i in range(10):
  t = ThreadClass()
  t.start()
