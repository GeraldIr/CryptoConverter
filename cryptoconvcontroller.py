# -*- coding: utf-8 -*-
"""
Created on Fri Sep  1 00:23:00 2017

@author: Gerald Walter Irsiegler
"""

import os
import time
#this is temporary I was too lazy to set up sheduling so I'm running this on my PC overnight until I do sheduling and I get a Raspberry Pi
#to run this on indefinitely and constantly
while True:
    os.system("cryptoconv.py")
    time.sleep(20)

