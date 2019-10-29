import pexpect
import sys
import sched, time
s = sched.scheduler(time.time, time.sleep)


def collect(count = 0):
    if count < 24:
        s.enter(120, 1, collect, argument=(count+1,))

    child = pexpect.spawn('python2.7 /home/wuxuejun0820/pytomo/start_crawl.py https://www.youtube.com/watch?v=J5pwZCcC8cg&t=22s')
    child.logfile = sys.stdout

    child.expect('Are you ok to start crawling?', timeout=9999)
    child.send('Y\n')
    child.expect('Press Enter to exit', timeout=9999999999)
    child.send('\n')


s.enter(120, 1, collect, argument=(0,))
s.run()
