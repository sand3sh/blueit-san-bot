import csv
from tinydb import TinyDB, Query
import subprocess
import os, sys
import threading
#subprocess.call(['./run_linux.sh','-u','SnooCauliflowers8786','-p','SnooCauliflowers87861986','-c','RPTmELs8EM1soA','-s','xFiyGi0XzCRoH-qRxSWqzmb0CQA','-a','script_by_snoo'], cwd="./blueit-san-bot-1")

db = TinyDB('/root/db.json')
db.truncate()

with open('acks.csv', 'r') as file:
    reader = csv.reader(file)
    cnt = 0
    for row in reader:
       cnt = cnt + 1
       #print(row)
       job = 'job'+str(cnt)
       db.insert({"job":job, "user":row[1], "password":row[2], "clientid":row[4], "clientsecret":row[5]})
       if(cnt == 3):
          cnt=0

time = 1.1 * 60 * 60

#job1 
print('Starting job1 with threads of each acc')
def startJob1():
    print('starting job1')
    job1 = db.search(Query().job == 'job1')
    for x in range(0, len(job1)):
        print(job1[x]['user'] + "  <---> "+"./blueit-san-bot-"+x)
        subprocess.call(['./run_linux.sh','-u',job1[x]['user'],'-p',job1[x]['password'],'-c',job1[x]['clientid'],'-s',job1[x]['clientsecret'],'-a','script_by_'+job1[x]['user']], cwd="./blueit-san-bot-"+x)

offset =  time * 0
t = threading.Timer(10.0+offset, startJob1)
t.start()

#job2 
print('Starting job2 with threads of each acc')
def startJob2():
    print('starting job2')
    job2 = db.search(Query().job == 'job2')
    for x in range(0, len(job2)):
        print(job2[x]['user'] + "  <---> "+"./blueit-san-bot-"+x)
        subprocess.call(['./run_linux.sh','-u',job2[x]['user'],'-p',job2[x]['password'],'-c',job2[x]['clientid'],'-s',job2[x]['clientsecret'],'-a','script_by_'+job2[x]['user']], cwd="./blueit-san-bot-"+x)

offset =  time * 1
t = threading.Timer(10.0+offset, startJob2)
t.start()


#print(db.all())
print('Main exite')