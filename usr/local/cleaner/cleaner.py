#!/usr/bin/env python
import sys, time
from daemon import Daemon
from cleanerproc import CleanerProc

class Cleaner(Daemon):
	cp = CleanerProc()
	
	def run(self):
		self.cp.init()
		while True:
			self.cp.process()
			time.sleep(3)

if __name__ == "__main__":
	daemon = Cleaner('/tmp/cleaner.pid')
	if len(sys.argv) > 1:
		action = sys.argv[1]
		if action in ["start", "stop", "restart"]:
			getattr(daemon, action)()
		else:
			print "usage: %s start|stop|restart" % sys.argv[0]
			sys.exit(2)
	else:
		print "usage: %s start|stop|restart" % sys.argv[0]
		sys.exit(1)
