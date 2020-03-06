# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 08:45:52 2019

@author: chloe.troupel
purpose: to fix a RDV to 2 process. We have to have 2 receivers and 1 emitter to have a RDV
"""

import multiprocessing as mp
import sys

def rdv1a2():
    print("rdv 1 to 2")

def emmetteur(semE,semR):
    print ("emitter produce a message and waits")
    mutex.acquire()    
    semR.acquire()
    semR.acquire()
    semE.release()
    semE.release()
    mutex.release()    
    rdv1a2()
    sys.exit(0)
    
def recepteur(semE,semR):
    semR.release()
    print("receiver and waits")
    semE.acquire() 
    sys.exit(0)
    
   
semE=mp.Semaphore(0)
semR=mp.Semaphore(0)
mutex=mp.Lock() 

l=[]
for i in ["E", "R", "R"]:
    if i == "E":
        pE=mp.Process(target= emmetteur, args= (semE,semR,))
        pE.start()
        l.append(pE)
    elif i == "R":
        pR=mp.Process(target= recepteur, args= (semE,semR,))
        pR.start()
        l.append(pR)

for p in l:
    p.join()
