import pexpect
import sys
import sched, time
from datetime import datetime
from threading import Timer

s = sched.scheduler(time.time, time.sleep)
x=datetime.today()
y=x.replace(day=x.day, hour=18, minute=0, second=0, microsecond=0)
delta_t=y-x
secs = delta_t.seconds+1

def collect(count = 0):
    print(datetime.now())
    if count < 24:
        s.enter(3600, 1, collect, argument=(count+1,))

    child = pexpect.spawn('python2.7 /home/wuxuejun0820/pytomo/start_crawl.py https://www.youtube.com/watch?v=J5pwZCcC8cg&t=22s')
    child.logfile = sys.stdout

    child.expect('Are you ok to start crawling?', timeout=9999)
    child.send('Y\n')
    child.expect('Press Enter to exit', timeout=9999999999)
    child.send('\n')


s.enter(secs, 1, collect, argument=(0,))
s.run()

