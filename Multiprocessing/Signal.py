# -*- coding: utf-8 -*-
"""
Created on Mon May 20 16:38:47 2019

@author: chloe.troupel
purpose: to use signal
"""

import os, time, signal


def fonc(s,frame):
    print("message intercepted")


if os.fork()==0:
    signal.signal(signal.SIGINT,fonc)
    while True:
        print("loop son")
        time.sleep(5)
else:
    for n in range(1,4):
        print("loop father")
        time.sleep(1)




    
