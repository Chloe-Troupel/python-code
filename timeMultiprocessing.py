# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 08:06:44 2019

@author: chloe.troupel
purpose: to compare the rapidity of multiprocessing for a sum
"""

import time,sys, math
import multiprocessing as mp

arr=mp.Array("i",range(10))

#without processus

begin1=time.time()
Sum=sum(arr)
end1=time.time()

print ("The time without processus : ",end1-begin1, "The sum is ", Sum)

#with processus

nbproc=1#int(sys.argv[1])

def tableau(arr, nbproc,i):
        d=math.ceil(i*longT)
        f=math.ceil((i+1)*longT)
        L=arr[d:f]
        mutex.acquire()
        Sum.value += sum(L)
        print(Sum)
        mutex.release()
    
mutex=mp.Lock()
Sum=mp.Value('i',0)
liste=[]
longT=(len(arr)/nbproc)

begin2=time.time()
for i in range(nbproc):
    p=mp.Process(target= tableau, args= (arr,nbproc,i,))
    liste.append(p)
for p in liste:
    p.start()
for p in liste:
    p.join()
end2=time.time()

print("The time with processus : ",end2-begin2, "The sum is ", Sum.value)

assert(Sum.value==sum(arr))
