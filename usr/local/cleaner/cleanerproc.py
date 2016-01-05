import os, sys, time, shutil, httplib, urllib, logging

MAX = 4000000000 # 4G
DIR = '/srv' 

class CleanerProc(object):
    def init(self):
	logging.basicConfig(filename="/tmp/cleaner.log",level=logging.DEBUG)
    
    def process(self):
	try:
	    s, old = self.walk()
	    if s > MAX: 
		logging.debug("Need more free space: %d > %d" % (s, MAX))
		if len(old) > 1: 
		    logging.debug("Remove file: " + os.path.join(DIR, old))
		    os.remove(os.path.join(DIR, old))
		else: 
		    logging.debug("Olf files not found! PANIC!!!")
        except BaseException: 
	    logging.debug('Main cycle fail ' + str(sys.exc_info())) 
	    pass

    def walk(self):
	s = 0
	od = time.localtime()
	of = ""
	for root, dirs, files in os.walk(DIR):
	    for f in files:
		fn = os.path.join(root, f)
		s = s + os.path.getsize(fn)
		if os.path.getctime(fn) < od:
		    of = fn
		    od = os.path.getctime(fn)
	return s, of

# Test
#cp = CleanerProc()
#cp.init()
#cp.process()