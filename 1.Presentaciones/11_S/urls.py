import urllib2
import time

hosts = [   "http://yahoo.com",
            "http://google.com",
            "http://amazon.com",
            "http://ibm.com",
            "http://apple.com",
            "http://www.eafit.edu.co",
            "http://unalmed.edu.co",
            "http://yahoo.com",
            "http://google.com",
            "http://amazon.com",
            "http://ibm.com",
            "http://apple.com",
            "http://www.eafit.edu.co",
            "http://unalmed.edu.co",
            "http://yahoo.com",
            "http://google.com",
            "http://amazon.com",
            "http://ibm.com",
            "http://apple.com",
            "http://www.eafit.edu.co",
            "http://unalmed.edu.co",
            "http://yahoo.com",
            "http://google.com",
            "http://amazon.com",
            "http://ibm.com",
            "http://apple.com",
            "http://www.eafit.edu.co",
            "http://unalmed.edu.co"
        ]

start = time.time()

for host in hosts:
    url = urllib2.urlopen(host)
    print url.read(1024)

print "Elapsed Time: %s" % (time.time() - start)
