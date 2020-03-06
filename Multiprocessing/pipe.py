# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 2019

@author: chloe.troupel
purpose: to use pipe
"""
import sys, os
import multiprocessing as mp

T=(100,200,300)
(dfr,dfw) = mp.Pipe()

pid=os.fork()

if pid != 0:
    dfr.close()
    n=dfw.send(T)
    print("[The process %d] transmitted the message %s\n" %(os.getpid(),T))
    dfw.close()
    
else:
     dfw.close()
     msgReception=dfr.recv()
     print("[The process %d] received the message %s\n" %(os.getpid(),msgReception))
     dfr.close()
