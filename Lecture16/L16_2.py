#!/user/bin/python3

import os,sys
import numpy as np
import matplotlib.pyplot as plt

align = open("alignment.txt").read().upper()

for each_line in align:
    len_seq = len(each_line)
    
  
