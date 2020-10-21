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
    os.system('kill %d'%pid)
    os.system('echo %s >> /root/killedbyPyPids'%pid)
#3 Hours
t = threading.Timer(10800.0, quit_system)
t.start()
#code to auto terminate the bot after 3 hours

if __name__ == "__main__":

  p1 = Process(target=webapp.run)
  p1.start()
  init.init()