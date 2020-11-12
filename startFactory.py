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
       print('Adding ',"job"+str(job),"user "+row[1])
       if(cnt == 3):
          cnt=0

time = 1.1 * 60 * 60

#job1 
print('MAIN:[Initializing Job] 1')
def startJob1():
    print('Starting job1')
    job1 = db.search(Query().job == 'job1')
    for x in range(0, len(job1)):
        print(job1[x]['user'] + "  <---> "+"./blueit-san-bot-"+str(x))
        subprocess.call('nohup ./run_linux.sh -u'+job1[x]['user']+' -p '+job1[x]['password']+' -c '+job1[x]['clientid']+' -s '+job1[x]['clientsecret']+' -a script_by_'+job1[x]['user']+' & echo $! > run.pid', cwd="../blueit-san-bot-"+str(x),shell=True)

        #subprocess.call(['./run_linux.sh','-u',job1[x]['user'],'-p',job1[x]['password'],'-c',job1[x]['clientid'],'-s',job1[x]['clientsecret'],'-a','script_by_'+job1[x]['user']], cwd="../blueit-san-bot-"+str(x))
        print('running '+job1[x]['user'])

offset =  time * 0
t = threading.Timer(10.0+offset, startJob1)
t.start()

#job2 
print('MAIN:[Initializing Job] 2')
def startJob2():
    print('Starting job2')
    job2 = db.search(Query().job == 'job2')
    for x in range(0, len(job2)):
        print(job2[x]['user'] + "  <---> "+"./blueit-san-bot-"+str(x))
        subprocess.call(['./run_linux.sh','-u',job2[x]['user'],'-p',job2[x]['password'],'-c',job2[x]['clientid'],'-s',job2[x]['clientsecret'],'-a','script_by_'+job2[x]['user']], cwd="../blueit-san-bot-"+str(x))

offset =  time * 1
t = threading.Timer(10.0+offset, startJob2)
t.start()

#job3
print('MAIN:[Initializing Job] 3')
def startJob3():
    print('Starting job3')
    job3 = db.search(Query().job == 'job3')
    for x in range(0, len(job3)):
        print(job3[x]['user'] + "  <---> "+"./blueit-san-bot-"+str(x))
        subprocess.call(['./run_linux.sh','-u',job3[x]['user'],'-p',job3[x]['password'],'-c',job3[x]['clientid'],'-s',job3[x]['clientsecret'],'-a','script_by_'+job3[x]['user']], cwd="../blueit-san-bot-"+str(x))

offset =  time * 2
t = threading.Timer(10.0+offset, startJob3)
t.start()

#print(db.all())
print('Main exited')
