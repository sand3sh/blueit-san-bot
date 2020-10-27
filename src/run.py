import init
import os, sys
import threading
from web import webapp
from multiprocessing import Process

#code to auto terminate the bot after 3 hours
pid = os.getpid()
print(pid)
os.system('echo %s >> /root/pids'%pid)
def quit_system():
    os.system('echo %s >> /root/killedbyPyPids'%pid)
    os.system('kill %d'%pid)
#3 Hours
time = 1 * 60 * 60
t = threading.Timer(time, quit_system)
t.start()
#code to auto terminate the bot after 3 hours

if __name__ == "__main__":

  p1 = Process(target=webapp.run)
  p1.start()
  init.init()